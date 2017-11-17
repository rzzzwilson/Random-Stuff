#!/bin/env python

"""
A program to backup the NOTEBOOK USB stick. Runs from either
the CLI or GUI.

Usage: nb
"""

import os
import time
import shutil
import platform
import logger
from tkinter_error import tkinter_error
from subprocess import Popen, PIPE, STDOUT

# Requirements:
#   . Runs under either python2 or 3
#   . Runs in CLI or a GUI
#   . Must find mounted NOTEBOOK automatically
#   . As easy to use and as error-proof as possible
#   . Saves NOTEBOOK in time+date stamped directory
#   . Save directory must not exceed defined size limit
#   . Check the NOTEBOOK filesystem for errors

# where we store the backups
BACKUP_BASE = os.path.expanduser('~/NOTEBOOK_Backups')

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
    return (process.returncode, output)

def say(msg):
    """Say a message through the voice synthesizer.

    msg  the message to say
    """

    pass

def abort(msg, status=1):
    """
    Display an abort dialog.

    msg  message to display

    Exits with an error status.
    """

    tkinter_error(msg)
    sys.exit(status)

def check_filesystem(device, mount_point):
    """
    Check the filesystem for  device.

    device       the device to check
    mount_point  where the device is mounted
    """

    say('File system check')
    print('Performing filesystem check on %s ... ' % device)

    if UName == 'Linux':
        (res, _) = do_cmdline(['umount', '%s' % mount_point])
        if res != 0:
            abort("Couldn't umount device at %s" % mount_point)
        (res, _) = do_cmdline(['sudo', 'fsck', '%s' % device])
        if res != 0:
            say("Filesystem errors")
            abort("Errors when running 'fsck' on device '%s'" % device)
        print('OK!')
    elif UName == 'Darwin':
        (res, _) = do_cmdline(['diskutil', 'repairVolume', '%s' % mount_point])
        if res != 0:
            say("Filesystem errors")
            abort("Errors when running 'diskutil' on device at '%s'" % mount_point)
        (res, _) = do_cmdline(['diskutil', 'unmount', '%s' % device])
        if res != 0:
            say("Dismount failed")
            abort("Dismount of device '%s' failed!?" % device)
        print('OK!')
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
            elif UName == 'Darwin':
                device = fields[0]
                mount = fields[8]
            else:
                return None

    return (device, mount)

def main(fs_check):
    """Backup the memory stick, if found.
    """

    # get device and mount point
    result = get_device_mount(NOTEBOOK)
    if result is None:
        log("No mounted device called '%s'" % NOTEBOOK)
        abort("Sorry, the NOTEBOOK '%s' isn't mounted." % NOTEBOOK)
    (device, mount) = result

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

# # copy NOTEBOOK to backup
# echo "Copying NOTEBOOK to $BACKUP_DIR"
# rsync -q --links -r $MOUNT/* $BACKUP_DIR
# cp $MOUNT/.diskid $BACKUP_DIR

    src_path = os.path.join(mount, '*')
    (status, output) = do_cmdline(['rsync', '-q', '--links', '-r', src_path, target_dir])

    # filesystem check?
    if fs_check:
        check_filesystem(device, mount)

    # limit backup dir size

    return 0


if __name__ == '__main__':
    import sys
    import getopt
    import traceback

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
        (opts, args) = getopt.getopt(argv, 'd:h', ['debug=', 'help'])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(1)

    fs_check = True             # do filesystem check

    for (opt, param) in opts:
        if opt in ['-f', '--fs_check']:
            fs_check = False
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # run the program code
    result = main(fs_check)
    sys.exit(result)

