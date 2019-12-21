#!/usr/bin/env python3

"""
A program to backup from one or more source directories (local or external)
to a designated "backup" external drive.

usage: backup [-f] [-h]

where -d <level>  sets debug to <level> ("debug", "info", etc)
      -f          disable fsck of the target BACKUP media
      -h          prints this help

To restore:
    /usr/local/bin/rsync  -aE -r --protect-args ./ /Volumes/DATA/
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
#           ('/Volumes/MusicPhotos', '.diskid', 'musicphotos'),
          ]

# target directory and drive information
# (path, id_file, id_string)
Target = ('/Volumes/BACKUP', '.diskid', 'backup 2.2')

# number of old backups to keep
NumOldBackups = 15

# maximum target used space before deleting old backups (%)
MaxPercentUsed = 95

# files extensions we DON'T backup (damn Apple...)
ExcludeFiles = ['.DS_Store', '.Trashes', '.fseventsd',
                '.DocumentRevisions-V100', '.TemporaryItems',
                '.DocumentRevisions-V100-bad-1', '.Spotlight-V100']


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

dict_debug_level = {
                    'CRITICAL': logger.Log.DEBUG,
                    'ERROR': logger.Log.ERROR,
                    'WARN': logger.Log.WARN,
                    'INFO': logger.Log.INFO,
                    'DEBUG': logger.Log.DEBUG,
                   }


def usage(msg=None):
    """Print usage with an optional 'msg'."""

    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)
    print(__doc__)


def abort(msg):
    """Abort the backup, display 'msg'."""

    log.critical('Abort: ' + msg)
    print(msg)
    cmd = ('osascript -e "display dialog \\"%s\\" buttons {\\"OK\\"} '
           'default button \\"OK\\"" >/dev/null 2>&1' % (msg))
    os.system(cmd)
    sys.exit(1)


def say(msg):
    """Speak the error message."""

    cmd = 'say "%s"' % (msg)
    os.system('say "%s"' % msg)


def alert(msg):
    """Display problem information."""

    log.critical(f'Alert: {msg}')
    print(msg)
    cmd = ('osascript -e "display dialog \\"%s\\" buttons {\\"OK\\"} '
           'default button \\"OK\\"" >/dev/null 2>&1' % (msg))
    os.system(cmd)


def get_space_used_remain(target):
    """Get used and remaining space on a filesystem.

    target is the root of the desired filesystem.

    Returns a tuple (used, remaining) which is the percent integer values
    for used and remaining disk space, respectively.
    """

    try:
        result = subprocess.check_output(['df', target]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        log.critical('get_space_used_remain: Error getting space remaining')
        say('Error getting space remaining')
        print("Error getting space remaining")
        abort(f'Error status {e.returncode}')

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

    log.debug(f'prune_target_size: target={target}, max_percent={max_percent}')

    # get list of existing directories, sorted
    path = os.path.join(target, '[0-9][0-9][0-9][0-9]*')
    dirs = glob.glob(path)
    dirs.sort()
    log.debug(f'prune_target_size: dirs={dirs}')

    # now keep deleting oldest until we are under the limit
    while len(dirs) > 1:
        # get free space percentage
        (used, _) = get_space_used_remain(target)

        # if enough space free, bomb out
        if used < max_percent:
            break

        # get oldest directory remaining, remove from dir list
        oldest_dir = dirs.pop(0)

        # delete the directory
        cmd = f'rm -Rf "{oldest_dir}"'
        log.debug(f"prune_target_size: deleting '{oldest_dir}'")
        os.system(cmd)


def create_target(target):
    """Create a target directory 'target'.

    target  path to the base directory for backup

    Return the path to the newly target directory.
    """

    try:
        log.info(f'create_target: os.makedirs({target})')
        os.makedirs(target)
    except PermissionError as e:
        say('Error creating target directory')
        abort(f"Error creating target '{target}'\n{e}")

    return target


def get_links_dir(target, bname):
    """Get a links directory.

    target  path to target base
    bname   basename of backup (eg, 'YouTube')

    The backup directory structure is:
        /device/path/dir1/ebooks
                             /20180818_092546
                             /20180819_104523
                             /20180821_120348

    Returns an absolute path to the youngest directory to use for links.
    Return None if no candidate directories.
    """

    log.debug(f'get_links_dir: target={target}, bname={bname}')

    path = os.path.join(target, bname, '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_*')
    log(f'get_links_dir: path={path}')
    dirs = glob.glob(path)
    dirs.sort()
    log.debug(f'get_links_dir: dirs={dirs}')

    # we have to look inside each dated backup dir to see if 'bname' is there
    # look in youngest first, then next youngest, etc
    for path in dirs[::-1]:
        log.debug(f'get_links_dir: checking path {path}')
        if os.path.isdir(path):
            log.debug(f'get_links_dir: returning path={path}')
            return path

    log.debug('get_links_dir: returning None')
    return None


def do_backup(code_path, sources, target_base):
    """Perform a backup.

    code_path    path to the executable doing the backup
    sources      list of tuples (path, id_file, id_string)
    target_base  base target path (like /device/path/)

    The target directory to put a backup into will be calculated
    from each source directory.
    """

    log.info(f'do_backup: code_path={code_path}, sources={sources}, target_base={target_base}')

    # create the timestamp string
    timestamp = time.strftime('%Y%m%d_%H%M%S')

    # exclude all files not to be handled
    exclude = ''
    for f in ExcludeFiles:
        exclude += f' --exclude="{f}"'
    log.debug(f"do_backup: exclude='{exclude}'")

    # backup each source dir
    for s in sources:
        (source_path, source_idfile, source_idstring) = s

        # check that the source is available
        log.info(f"do_backup: source dir='{source_path}'")
        if not check_available(source_path, source_idfile, source_idstring):
            print(f"Skipping source '{source_path}' - not available")
            say(f'Skipping source {source_path}')
            log.info(f"Skipping source '{source_path}' - not available")
            continue

        # figure out the actual target dir for this source
        source_basename = os.path.basename(source_path)
        target_dir = os.path.join(target_base, source_basename, timestamp)
        log.debug(f'do_backup: target_dir={target_dir}')

        # get links dir, depending on source
        links_dir = get_links_dir(target_base, source_basename)

        # ensure that 'target_dir' and 'links_dir' are absolute paths
        target_dir = os.path.abspath(target_dir)
        if links_dir:
            links_dir = os.path.abspath(links_dir)
        log.info(f"do_backup: target_dir='{target_dir}', "
                 f"links_dir='{links_dir}'")

        # create the target directory
        create_target(target_dir)

        # copy this backup code to target path
        cmd = f'cp "{code_path}" "{target_dir}"'
        log.debug(f"do_backup: doing '{cmd}'")
        os.system(cmd)

        # actually do the backup now
        if links_dir:
            cmd = (f'{RsyncPath} {RsyncOptions} {exclude} '
                   f'--link-dest="{links_dir}" "{source_path}/" "{target_dir}/"')
        else:
            cmd = (f'{RsyncPath} {RsyncOptions} {exclude} '
                   f'"{source_path}/" "{target_dir}/"')
        log.debug(f"do_backup: cmd='{cmd}'")
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
        log.info(f"check_available: Filesystem '{path}' isn't available?")
        return False

    # return success here if we have no 'id_string'
    if id_string is None:
        return True

    # get complete path to ID file and check it's there
    id_file = os.path.join(path, id_file)
    if not os.path.isfile(id_file):
        log.info(f"check_available: Can't find ID file '{id_file}'")
        return False

    # check contents of disk ID file
    with open(id_file, 'r') as f:
        data = f.read()
    data = data.strip()
    if data != id_string:
        log.info(f"check_available: ID file '{id_file}' contains '{data}', "
                 f"expected '{id_string}'")
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
        say('Error getting device for mounted file system')
        print(f"Error getting device for mounted filesystem, check log in file '{LogFile}'")
        log(f"Error getting device for mounted filesystem")
        abort(f'Error status {e.returncode}')

    for line in result.split('\n'):
        if path in line:
            data = line.split()[0]
            log.info(f'get_device: filesystem {path} is on device {data}')
            return data

    raise RuntimeError(f"No device found for '{path}'")


def check_filesystem(fs_base):
    """Check the target filesystem for errors.

    fs_base  path to the base of the filesystem to check
    """

    log.info(f'Checking filesystem for target {fs_base}')

    # get device for the target filesystem
    device = get_device(fs_base)

    # check filesystem
    log.debug(Delim1)
    cmd = f'diskutil repairVolume {device}'
    log.debug(f"fsck command='{cmd}'")
    cmd = cmd.split()

    try:
        result = subprocess.check_output(cmd).decode("utf-8")
    except subprocess.CalledProcessError as e:
        say('Error found when checking file system')
        print(f"Error found when checking filesystem, check log in file '{LogFile}'")
        abort(f'Error found when checking filesystem on {fs_base} ({device}), error status {e.returncode}')

    log.debug(result)
    log.debug(Delim2)


def backup(fsck, code_path, sources, target, max_percent, exclude_files):
    """Perform the backup.
    
    fsck           True if we need to do 'fsck' check of target volume
    code_path      path to this code file
    sources        list of tuples (path, id_file, id_string)
    target         tuple (path, id_file, id_string)
    max_percent    maximum percent of target used before pruning
    exclude_files  list of source files that are excluded from backup
    """

    # unpack the target information
    (target_base, target_idfile, target_idstring) = target

    # check that the target filesystem is available
    if not check_available(*target):
        say('Target file system not found')
        abort(f'{target_base} not mounted or disk ID file not found.')

    # delete old directories, if required, until below configured size
#    prune_target_size(target_base, max_percent)

    # do the backup
    do_backup(code_path, sources, target_base)

    # check source and target filesystems, if required
    if fsck:
        check_filesystem(target_base)

    return 0

def del_old_backups(sources, target):
    """Delete backups until we have the specified maximum number.

    sources  a list of tuples, one for each source
    target  tuple holding target information
            (path, diskid, label)
    """

    # unpack the target information
    (target_base, target_idfile, target_idstring) = target

    log.info(f'Deleting old backups on {target_base}')

    for (src, _, _) in Sources:
        target_dir = os.path.basename(src)
        work_dir = os.path.join(target_base, target_dir)

        # delete old backup directories if more than NumOldBackups
        result = subprocess.check_output(['ls', work_dir]).decode("utf-8")
        result = result.split()
        result.sort()
        num_backups = len(result)
        if num_backups > NumOldBackups:
            for path in result[:num_backups - NumOldBackups]:
                del_path = os.path.join(work_dir, path)
                log.info(f"Deleting '{del_path}' ...")
                result = subprocess.check_output(['rm','-Rf', del_path]).decode("utf-8")
                if result:
                    log.info(f"result={result}")


if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    start_time = time.time()

    # remember where we are in the filesystem
    # we come back to this place when finished
    current_dir = os.getcwd()

    # move to a 'neutral' place - the user's home directory
    home = os.path.expanduser('~')
    os.chdir(home)

    # a function to print 'human time' given a delta
    def human_time(delta):
        delta = int(delta)
        (minutes, seconds) = divmod(delta, 60)
        (hours, minutes) = divmod(minutes, 60)

        return f'{hours}:{minutes:02d}:{seconds:02d}'

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
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'd:fh',
                                     ['debug=', 'fsck', 'help'])
    except getopt.GetoptError as err:
        usage(err)
        os.chdir(current_dir)
        sys.exit(1)

    # default parameters
    fsck = True                 # always check target filesystem
    debug = logger.Log.DEBUG    # log at DEBUG level

    for (opt, param) in opts:
        if opt in ['-d', '--debug']:
            debug = param.upper()
            if debug not in dict_debug_level:
                usage(f"Debug level '{param}' not recognized")
                os.chdir(current_dir)
                sys.exit(1)
            debug = dict_debug_level[debug]
        if opt in ['-f', '--fsck']:
            fsck = False
        elif opt in ['-h', '--help']:
            usage()
            os.chdir(current_dir)
            sys.exit(0)

    # get absolute path to this file
    code_path = os.path.abspath(__file__)

    # set up logging
    log = logger.Log(LogFile, debug)

    # run the program code
    res = backup(fsck, code_path, Sources, Target, MaxPercentUsed, ExcludeFiles)

    # delete old backups
    del_old_backups(Sources, Target)

    # check source disk(s), always
    for (src, _, _) in Sources:
        check_filesystem(src)

    # report on space left on target
    (target_base, _, _) =  Target
    (_, target_left) = get_space_used_remain(target_base)
    remaining_msg = f'Space remaining on {target_base} = {target_left}%'
    log.info(remaining_msg)
    print(remaining_msg)

    delta_time = time.time() - start_time
    print(f'Total time: {human_time(delta_time)}')

    log.info('Backup finished')
    say('Backup finished')

    # change back to the directory we started in
    os.chdir(current_dir)

    sys.exit(res)
