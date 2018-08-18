#!/usr/bin/env python3

"""
A program to backup from one or more source directories (local or external)
to a designated "backup" external drive.

usage: backup [-f] [-h]

where -f forces a final fsck of the BACKUP media (can be 5 hours or so!),
and   -h prints this help
"""

import sys
import os
import os.path
import time
import glob
import subprocess
import logger


##########
# Config data
##########

# source directories and drive information
# [(path, id_file, id_string), ...]
Sources = [
           ('/Volumes/DATA', '.diskid', 'data'),
           ('/Volumes/MusicPhotos', '.diskid', 'musicphotos'),
          ]

# target directory and drive information
# (path, id_file, id_string)
Target = ('/Volumes/BACKUP', '.diskid', 'backup 2.1')

# maximum target used space before deleting old backups (%)
MaxPercentUsed = 95

# files extensions we DON'T backup (damn Apple...)
ExcludeFiles = ['.DS_Store', '.Trashes', '.fseventsd',
                '.DocumentRevisions-V100', '.TemporaryItems']

##########
# End of config data
##########

# name and version of this mess
ProgName = 'backup'
ProgVersion = '2.1'

# the logging file
LogFile = os.path.expanduser(f'~/{ProgName}.log')

# path to the 'rsync' to use
RsyncPath = '/usr/local/bin/rsync'

# miscellaneous
Delim1 = '#' * 60
Delim2 = '-' * 60

RsyncOptions = '-aE -r --protect-args'

# set up logging
log = logger.Log(LogFile, logger.Log.DEBUG)


def usage(msg=None):
    """Print usage with an optional 'msg'."""
    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)
    print(__doc__)

def abort(msg):
    """Abort the backup, display 'msg'."""

    log('Abort: ' + msg)
    print(msg)
    cmd = 'osascript -e "display dialog \\"%s\\" buttons {\\"OK\\"} default button \\"OK\\"" >/dev/null 2>&1' % (msg)
    os.system(cmd)
    sys.exit(1)

def say(msg):
    """Speak the error message."""

    cmd = 'say "%s"' % (msg)
    os.system('say "%s"' % msg)

def alert(msg):
    """Display problem information."""

    log(f'Alert: {msg}')
    print(msg)
    cmd = 'osascript -e "display dialog \\"%s\\" buttons {\\"OK\\"} default button \\"OK\\"" >/dev/null 2>&1' % (msg)
    os.system(cmd)

def get_space_used_remain(target):
    """Get used and remaining space on a filesystem.

    target is the root of the desired filesystem.

    Returns a tuple (used, remaining) which is the percent integer values
    for used and remaining disk spaxe, respectively.
    """

    try:
        result = subprocess.check_output(['df', target]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        say('Error doing backup')
        print(f"Error doing backup, check log in file '{LogFile}'")
        abort(f'Error status {e.returnerror}\n{e.output}')

    result = result.split('\n')[-2]
    result_split = result.split()
    space_available = int(result_split[1])
    space_used = int(result_split[2])
    remain = int((space_available - space_used) / space_available * 100)
    used = int(space_used / space_available * 100)
    return (used, remain)

def prune_target_size(target, max_percent):
    """Check 'target' size and prune if above limit.

    target       path to the target disk
    max_percent  maximum percent used allowed
    """

    log(f'prune_target_size: target={target}, max_percent={max_percent}')

    # get list of existing directories, sorted
    path = os.path.join(target, '[0-9][0-9][0-9][0-9]*')
    dirs = glob.glob(path)
    dirs.sort()
    log(f'prune_target_size: dirs={dirs}')

    # now keep deleting oldest until we are under the limit
    while len(dirs) > 1:
        # get free space percentage
        (used, remain) = get_space_used_remain(target)

        # if enough space free, bomb out
        if used < max_percent:
            break

        # get oldest directory remaining, remove from dir list
        oldest_dir = dirs.pop(0)

        # delete the directory
        cmd = f'rm -Rf "{oldest_dir}"'
        log(f"prune_target_size: deleting '{oldest_dir}'")
        os.system(cmd)

def create_target(target, source):
    """Create a target directory 'target'.

    target  path to the base directory for backup
    source  source filesystem basename

    Return the path to the newly target directory.
    """

    log(f"create_target: target={target}, source={source}")
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    path = os.path.join(target, timestamp)
    try:
        log(f'create_target: os.makedirs({path}')
        os.makedirs(path)
    except PermissionError as e:
        say('Error creating target directory')
        abort(f"Error creating target '{path}'\n{e}")
    return path

def get_links_dir(tvol):
    """Get a links directory.

    tvol  path to target

    Returns an absolute path to the youngest directory to use for links.
    The target directory already created, so skip youngest.
    Return None if no candidate directories.
    """

    log(f'get_links_dir: tvol={tvol}')

    path = os.path.join(tvol, '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_*')
    log(f'get_links_dir: path={path}')
    dirs = glob.glob(path)
    dirs.sort()
    log(f'get_links_dir: dirs={dirs}')
    if len(dirs) > 1:
        return dirs[-2]
    return None

def do_backup(code_path, sources, target_dir):
    """Perform a backup.

    code_path   path to the executable doing the backup
    sources     list of tuples (path, id_file, id_string)
    target_dir  the top-level target directory to put a backup into

    The target directory to put a backup into will be calculated
    from each source directory.
    """

    # exclude all files required
    exclude = ''
    for f in ExcludeFiles:
        exclude += f' --exclude="{f}"'
    log(f"do_backup: exclude='{exclude}'")

    # backup each source dir
    for s in sources:
        (source_path, source_idfile, source_idstring) = s

        # check that the source is available
        log(f"do_backup: source dir='{source_path}'")
        if not check_available(source_path, source_idfile, source_idstring):
            print(f"Skipping source '{source_path}' - not available")
            say(f'Skipping source {source_path}')
            log(f"Skipping source '{source_path}' - not available")
            continue

        # figure out the actual target dir for this source
        source_basename = os.path.basename(source_path)
        base_target_dir = os.path.join(target_dir, source_basename)
        log(f"do_backup: base_target_dir='{base_target_dir}'")

        # get links dir and target dir depending on source
        backup_dir = create_target(base_target_dir, source_basename)
        log(f"backup: backup_dir='{backup_dir}'")

        links_dir = get_links_dir(base_target_dir)
        log(f"backup: links_dir='{links_dir}'")

        # ensure that 'backup_dir' and 'links_dir' are absolute paths
        backup_dir = os.path.abspath(backup_dir)
        if links_dir:
            links_dir = os.path.abspath(links_dir)
        log(f"do_backup: backup_dir='{backup_dir}', links_dir='{links_dir}'")

        # copy this backup code to target dir
        cmd = f'cp "{code_path}" "{backup_dir}"'
        log(cmd)
        os.system(cmd)

        # actually do the backup now
        if links_dir:
            log(f"links_dir='{links_dir}'")
            cmd = f'{RsyncPath} {RsyncOptions} {exclude} --link-dest="{links_dir}" "{source_path}/" "{backup_dir}/"'
        else:
            cmd = f'{RsyncPath} {RsyncOptions} {exclude} "{source_path}/" "{backup_dir}/"'
        log(f"do_backup: cmd='{cmd}'")
        os.system(cmd)

def check_available(path, id_file, id_string=None):
    """Check that the given filesystem is available.

    path       path to the drive
    id_file    name of the ID file
    id_string  expected contents of the id_file

    If 'id_string' is None, don't check ID file.
    Returns True if all OK, else False.
    """

    # is the filesystem itself available?
    if not os.path.isdir(path):
        log(f"check_available: Filesystem '{path}' isn't available?")
        return False

    # return success here if we have no 'id_string'
    if id_string is None:
        return True

    # get complete path to ID file and check it's there
    id_file = os.path.join(path, id_file)
    if not os.path.isfile(id_file):
        log(f"check_available: Can't find ID file '{id_file}'")
        return False

    # check contents of disk ID file
    with open(id_file, 'r') as f:
        data = f.read()
    data = data.strip()
    if data != id_string:
        log(f"check_available: ID file '{id_file}' contains '{data}', expected '{id_string}'")
        return False

    return True

def get_device(path):
    """Get the device for a mounted filesystem.

    path  path to root of mounted filesystem

    Returns the device.
    """

    try:
        result = subprocess.check_output(['df', '-h', path]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        say('Error getting device for mounted filesystem')
        print(f"Error getting device for mounted filesystem, check log in file '{LogFile}'")
        abort(f'Error status {e.returnerror}\n{e.output}')

    for line in result.split('\n'):
        if path in line:
            data = line.split()[0]
            return data
    raise RuntimeError(f"No device found for '{path}'")

def backup(fsck, code_path, sources, target, max_percent, exclude_files):
    """Perform the backup.
    
    fsck           True if we need to do 'fsck' check of target volume
    code_path      path to this code file
    sources        list of tuples ((path, id_file, id_string)
    target         tuple (path, id_file, id_string)
    max_percent    maximum percent of target used before pruning
    exclude_files  list of source files that are excluded from backup
    """

    # unpack the target information
    (target_base, target_idfile, target_idstring) = target

    # check that the target filesystem is available
    if not check_available(target_base, target_idfile, target_idstring):
        say('Target filesystem not found')
        abort(f'{target_base} filesystem not mounted or disk ID file not found.')

    # delete old directories, if required
    prune_target_size(target_base, max_percent)

    # do the backup
    do_backup(code_path, sources, target_base)

    # check target filesystem, if required
    if fsck:
        # get device for the target filesystem
        device = get_device(target_base)
        log(f"backup: Device for '{target_base}' is '{device}'")

        # check filesystem
        log(f'backup: checking target filesystem {target_base}')
        log(Delim1)
        cmd = f'diskutil repairVolume {device}'
        log(f"backup: fsck command '{cmd}'")
        cmd = cmd.split()

        try:
            result = subprocess.check_output(cmd).decode("utf-8")
        except subprocess.CalledProcessError as e:
            say('Error checking filesystem')
            print(f"Error checking filesystem, check log in file '{LogFile}'")
            abort(f'Error status {e.returnerror}\n{e.output}')

        log(result)
        log(Delim2)

    # report on space left on target
    (_, target_left) = get_space_used_remain(target_base)
    remaining_msg = f'Space remaining on {target_base} = {target_left}%'
    log(remaining_msg)
    print(remaining_msg)

    log('Backup finished')
    say('Backup finished')

    return 0


if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        log(msg)
        print(msg)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'fh', ['fsck', 'help'])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(1)

    # default parameters
    fsck = False

    for (opt, param) in opts:
        if opt in ['-f', '--fsck']:
            fsck = True
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # get absolute path to this file
    code_path = os.path.abspath(__file__)

    # run the program code
    sys.exit(backup(fsck, code_path, Sources, Target, MaxPercentUsed, ExcludeFiles))
