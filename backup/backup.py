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
#import config as cfg

##########
# Config data
##########

# source/target dirs
Sources = ['/Volumes/DATA']
#Sources = ['./DATA']
Target = '/Volumes/BACKUP'
#Target = './BACKUP'

# maximum target used space before deleting old backups (%)
MaxPercentUsed = 95

# files extensions we DON'T backup (damn Apple...)
ExcludeFiles = ['.DS_Store', '.Trashes', '.fseventsd',
                '.DocumentRevisions-V100', '.TemporaryItems']

# name of the disk ID file and its expected contents
DiskIdFile = '.diskid'
DiskIdContents = 'backup 2.0'

##########
# End of config data
##########

# name and version of this mess
ProgName = 'backup'
ProgVersion = '2.0'

# name of the config file
ConfigFile = '.backup.cfg'

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

def create_target(target):
    """Create a target directory 'target'.

    Return the path to the new target directory.
    """

    log(f"create_target: target={target}")
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    path = os.path.join(target, timestamp)
    try:
        os.makedirs(path)
    except PermissionError as e:
        say('Error creating target directory')
        abort(f"Error creating target '{path}'\n{e}")
    return path

def get_links_dir(tvol):
    """Get a links directory.

    tvol  path to target

    Returns an absolute path to the youngest directory to use for links.
    Return None if no candidate directories.
    """

    path = os.path.join(tvol, '[0-9][0-9][0-9][0-9]*')
    dirs = glob.glob(path)
    dirs.sort()
    if dirs:
        return dirs[-1]
    return None

def do_backup(sources, target_dir, links_dir):
    """Perform a backup.

    target_dir  the target directory
    links_dir   abs path to the links directory (None if none used)
    """

    # ensure that 'target_dir' and 'links_dir' are absolute paths
    target_dir = os.path.abspath(target_dir)
    if links_dir:
        links_dir = os.path.abspath(links_dir)

    log(f"do_backup: target_dir='{target_dir}', links_dir='{links_dir}'")

    # exclude all files required
    exclude = ''
    for f in ExcludeFiles:
        exclude += f' --exclude="{f}"'
    log(f"do_backup: exclude='{exclude}'")

    # backup each source dir
    for s in sources:
        log(f"do_backup: source dir='{s}'")
        if not check_available(s):
            print(f"Skipping source '{s}' - not available")
            say(f'Skipping source {s}')
            log(f"Skipping source '{s}' - not available")
            continue

        # get basename of source as 'target_dir' directory name
        target_name = os.path.basename(s)
        target_path = os.path.join(target_dir, target_name)
        if links_dir:
            links_path = os.path.join(links_dir, target_name)

        # if that target directory exists, it's an error
        if os.path.isdir(target_path):
            msg = f"ERROR: target path {target_path}' already exists!?"
            print(msg)
            say('Internal error')
            abort(msg)

        # actually do the backup now
        os.system(f'mkdir -p "{target_path}"')
        if links_dir:
            log(f"links_path='{links_path}'")
            cmd = f'{RsyncPath} {RsyncOptions} {exclude} --link-dest="{links_path}" "{s}/" "{target_path}/"'
        else:
            cmd = f'{RsyncPath} {RsyncOptions} {exclude} "{s}/" "{target_path}/"'
        log(f"do_backup: cmd='{cmd}'")
        os.system(cmd)

def check_available(fspath, id_string=None):
    """Check that the given filesystem is available.

    fspath     path to the root of the filesystem
    id_string  string that should be in ID file

    If 'id_string' is None, don't check ID file.

    Returns True if all OK, else False.
    """

    # is the filesystem itself available?
    if not os.path.isdir(fspath):
        log(f"check_available: Filesystem '{fspath}' isn't available?")
        return False

    # return success here if we have no 'id_string'
    if id_string is None:
        return True

    # get complete path to ID file and check it's there
    id_file = os.path.join(fspath, DiskIdFile)
    if not os.path.isfile(id_file):
        log(f"check_available: Can't find ID file '{id_file}'")
        return False

    # check contents of disk ID file
    with open(id_file, 'r') as f:
        data = f.read()
    data = data.strip()
    if data != DiskIdContents:
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

def backup(fsck, code_path):
    """Perform the backup.
    
    fsck       True if we need to do 'fsck' check of target volume
    code_path  path to this code file
    """

    # check that the target filesystem is available
    if not check_available(Target, DiskIdContents):
        say('Target filesystem not found')
        abort(f'{Target} filesystem not mounted or disk ID file not found.')

    # delete old directories, if required
    prune_target_size(Target, MaxPercentUsed)

    # get links dir and target dir
    links_dir = get_links_dir(Target)
    log(f"backup: links_dir='{links_dir}'")
    target_dir = create_target(Target)
    log(f"backup: target_dir='{target_dir}'")

    # copy this backup code to target dir
    cmd = f'cp "{code_path}" "{target_dir}"'
    log(cmd)
    os.system(cmd)

    # do the backup
    do_backup(Sources, target_dir, links_dir)

    # check target filesystem, if required
    if fsck:
        # get device for the target filesystem
        device = get_device(Target)
        log(f"backup: Device for '{Target}' is '{device}'")

        # check filesystem
        log(f'backup: checking target filesystem {Target}')
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
    (_, target_left) = get_space_used_remain(Target)
    remaining_msg = f'Space remaining on {Target} = {target_left}%'
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
    recover = False

    for (opt, param) in opts:
        if opt in ['-f', '--fsck']:
            fsck = True
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # get absolute path to this file
    code_path = os.path.abspath(__file__)

    # run the program code
    sys.exit(backup(fsck, code_path))