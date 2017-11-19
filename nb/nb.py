#!/usr/bin/env python3

"""
A program to backup the NOTEBOOK USB stick.

Usage: nb
"""

import os
import sys
import time
import shutil
import platform
import logger
try:
    from tkinter_error import tkinter_error
except ImportError:
    tkinter_error = print
from subprocess import Popen, PIPE, STDOUT

# Requirements:
#   . Must find mounted NOTEBOOK automatically
#   . As easy to use and as error-proof as possible
#   . Saves NOTEBOOK in time+date stamped directory
#   . Save directory must not exceed defined size limit
#   . Check the NOTEBOOK filesystem for errors

# where we store the backups
#BACKUP_BASE = os.path.expanduser('~/NOTEBOOK_Backups')
BACKUP_BASE = os.path.expanduser('./NOTEBOOK_Backups')

# limit (GB) to total backup size on disk
LIMIT = 10

# delimiter print string
DELIM = "============================================================"

# get type of system we are running on
UName = platform.system()

NOTEBOOK = 'NOTEBOOK'
ID_FILE = '.diskid'
ID_STRING = 'NB 1.0'

if UName == 'Linux':
    ScriptPath = os.path.expanduser('~/bin/nb')
elif UName == 'Darwin':
    ScriptPath = os.path.expanduser('~/bin/nb')
else:
    abort("Don't handle Windows yet!")

def do_cmdline(cmd, text=''):
    """Execute program in 'cmd' and pass 'text' to STDIN.
    Returns a tuple of (status, result) where 'status' is the process
    exit status and 'result' is the STDOUT strip()ed output.
    Code from: https://stackoverflow.com/questions/8475290/how-do-i-write-to-a-python-subprocess-stdin
    Note that any prompt the program writes is included in STDOUT.
    """

    log('do_cmdline: cmd=%s' % str(cmd))

    process = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    output = process.communicate(input=bytes(text, 'utf-8'))[0].decode('utf-8').strip()
    log("do_cmdline: returns (%s, '%s')" % (str(process.returncode), str(output)))
    return (process.returncode, output)

def report(msg='\n'):
    """Print a message, special handling of '\n'.

    msg  the message to report on

    If 'msg' doesn't end with '\n' flush stdout.
    """

    print(msg, end='')
    if not msg.endswith('\n'):
        sys.stdout.flush()

def say(msg):
    """Say a message through the voice synthesizer.

    msg  the message to say
    """

    if Quiet:
        return

    if UName == 'Linux':
        log('Would say: %s' % msg)
    elif UName == 'Darwin':
        do_cmdline(['say', msg])
    elif UName == 'Windows':
        log('Would say: %s' % msg)

def abort(msg, status=1):
    """
    Display an abort dialog.

    msg  message to display

    Exits with an error status.
    """

    report()

    tkinter_error(msg)
    sys.exit(status)

def check_filesystem(device, mount_point):
    """
    Check the filesystem for  device.

    device       the device to check
    mount_point  where the device is mounted
    """

    say('File system check')
    report('Performing filesystem check on %s ... ' % device)

    if UName == 'Linux':
        (res, _) = do_cmdline(['umount', '%s' % mount_point])
        if res != 0:
            abort("Couldn't umount device at %s" % mount_point)
        (res, _) = do_cmdline(['sudo', 'fsck', '%s' % device])
        if res != 0:
            say("Filesystem errors")
            abort("Errors when running 'fsck' on device '%s'" % device)
        report('OK!\n')
    elif UName == 'Darwin':
        (res, output) = do_cmdline(['diskutil', 'repairVolume', '%s' % mount_point])
        if res != 0:
            say("Filesystem errors")
            if 'could not be unmounted' in output:
                abort("Diskutil couldn't unmount the NOTEBOOK!?")
            abort("Errors when running 'diskutil' on device at '%s'" % mount_point)
        (res, output) = do_cmdline(['diskutil', 'unmount', device])
        if res != 0:
            say("Dismount failed")
            abort("Dismount of device '%s' failed!?" % device)
        report('OK!\n')
    elif UName == 'Windows':
        abort("Don't handle Windows just yet")
    else:
        abort("Unrecognized platform: '%s'" % UName)

def total_size(directory):
    """Get total size of a directory in GB.

    directory  path to the directory
    """

    if UName == 'Linux':
        size = do_cmdline("""du -B g -d 0 %s | awk '{ print $1 }' | sed -e "s/G$//" """ % Base)
    elif UName == 'Darwin':
        size = do_cmdline("""du -g -d 0 $BACKUP_BASE | awk '{ print $1 }' """ % Base)
    elif UName == 'Windows':
        abort("Don't do Windows yet")

    return int(size)

def get_device_mount(name):
    """Get the device and mount point for a USB stick.

    name  the name of the USB stick

    Returns a tuple (device, mount) if found, else returns None.
    """

    # see what is mounted
    (status, df_line) = do_cmdline(['df', '-h'])
    if status != 0:
        return None

    # see if the required USB device is mounted
    for line in df_line.split('\n'):
        if name in line:
            fields = line.split()
            if UName == 'Linux':
                device = fields[0]
                mount = fields[5]
                return (device, mount)
            elif UName == 'Darwin':
                device = fields[0]
                mount = fields[8]
                return (device, mount)
            else:
                return None

    return None

def main(fs_check):
    """Backup the memory stick, if found.
    """

    # get device and mount point
    result = get_device_mount(NOTEBOOK)
    if result is None:
        log("No mounted device called '%s'" % NOTEBOOK)
        say("Memory stick isn't mounted")
        abort("Sorry, %s isn't mounted." % NOTEBOOK)
    (device, mount) = result
    log("main: device=%s, mount='%s'" % (device, mount))

    # check that the ID file is there, containing the correct string
    id_path = os.path.join(mount, ID_FILE)
    if not os.path.isfile(id_path):
        log("No file '%s' found" % id_path)
        abort("Sorry, the NOTEBOOK '%s' isn't mounted." % NOTEBOOK)
    with open(id_path, 'r') as fd:
        data = fd.read()
    data = data.strip()
    data = data.split('\n')
    if len(data) != 1 or data[0] != ID_STRING:
        log("ID file '%s' contained %s. expected ['%s']"
            % (id_path, str(data), ID_STRING))
        abort("Sorry, the NOTEBOOK '%s' isn't mounted." % NOTEBOOK)

# do we need this?
#    # OK, start copy.  First, copy this script to root of backup area
#    log('cp %s %s' % (ScriptPath, os.path.join(mount, 'files/computer/bin/')))
#    shutil.copy(ScriptPath, os.path.join(mount, 'files/computer/bin/'))

    # create the target directory with date+time stamp
    date_time = time.strftime('%Y%m%d_%H%M%S')
    target_dir = os.path.join(BACKUP_BASE, date_time)
    log("target_dir='%s'" % target_dir)
    os.makedirs(target_dir)

    # copy NOTEBOOK to backup
#    cp $MOUNT/.diskid $BACKUP_DIR
    log("Copy '%s' to '%s'" % (ID_FILE, target_dir))
    shutil.copy(os.path.join(mount, ID_FILE), target_dir)
    src_path = os.path.join(mount, '')
    log("src_path='%s'" % src_path)
    cmd_list = ['rsync', '-q', '--links', '-r', src_path, target_dir]
    log("sync: '%s'" % ' '.join(cmd_list))
    (status, output) = do_cmdline(cmd_list)

    # filesystem check?
    if fs_check:
        check_filesystem(device, mount)

    # limit backup dir size

    return 0


if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    global Quiet

    log = logger.Log('nb.log', logger.Log.DEBUG)

    def usage(msg=None):
        """Print a USAGE message with optional error message.
    
        msg  the optional error message
        """
    
        if msg:
            msg = msg.strip()       # remove terminal '\n', if any
            print('%s\n%s\n%s' % (DELIM, msg, DELIM))
        print(__doc__)
    
    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        log(msg)
        tkinter_error(msg)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'fhq', ['fs_check', 'help', 'quiet'])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(1)

    # default values
    fs_check = True             # do filesystem check
    Quiet = False               # speak progress

    for (opt, param) in opts:
        if opt in ['-f', '--fs_check']:
            fs_check = False
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['-q', '--quiet']:
            Quiet = True

    # run the program code
    result = main(fs_check)
    sys.exit(result)

