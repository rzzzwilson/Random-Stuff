#!/usr/bin/env python3

"""
A program to backup the NOTEBOOK USB stick.

Usage: nb
"""

import os
import sys
import time
import shutil
import string
import platform
import datetime
import traceback
from tkinter import *
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

'''
A small function to put an error message on the screen with Tkinter.

Used by GUI programs started from a desktop icon.
'''


def tkinter_error(msg, title=None):
    """Show an error message in a Tkinter dialog.

    msg    text message to display (may contain newlines, etc)
    title  the window title (defaults to 'ERROR')

    The whole point of this is to get *some* output from a python GUI
    program when run from an icon double-click.  We use Tkinter since it's
    part of standard python and we may be trying to say something like:

        +-----------------------------+
        |  you must install wxPython  |
        +-----------------------------+

    Under Linux and OSX we can run the program from the commandline and we would
    see printed output.  Under Windows that's hard to do, hence this code.

    NOTE: For some reason, Ubuntu python doesn't have tkinter installed as
    part of the base install.  Do "sudo apt-get install python-tk".
    """

    ######
    # Define the Application class
    ######

    class Application(Frame):
        def createWidgets(self):
            self.LABEL = Label(self, text=self.text, font=("Courier", 14))
            self.LABEL["fg"] = "black"
            self.LABEL["bg"] = "yellow"
            self.LABEL["justify"] = "left"
            self.LABEL.pack()

        def __init__(self, text, master=None):
            self.text = text
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()
            self.tkraise()


    # set the title string
    if title is None:
        title = 'ERROR'

    # get the message text
    msg = '\n' + msg.strip() + '\n'

    msg = msg.replace('\r', '')
    msg = msg.replace('\n', '   \n   ')

    app = Application(msg)
    app.master.title(title)
    app.mainloop()


"""
A simple logger.

Simple usage:
    import logger
    log = logger.Log('my_log.log', logger.Log.DEBUG)
    log('A line in the log at the default level (DEBUG)')   # simple
    log('A log line at WARN level', logger.Log.WARN)        # hard to use
    log.info('log line issued at INFO level')               # best if using level

Based on the 'borg' recipe from [http://code.activestate.com/recipes/66531/].

Log levels styled on the Python 'logging' module.

Log output includes the module and line # of the log() call.
"""


################################################################################
# A simple (?) logger.
################################################################################

class Log(object):

    __shared_state = {}                # this __dict__ shared by ALL instances

    # the predefined logging levels
    CRITICAL = 50
    ERROR = 40
    WARN = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    MAXLEVEL = CRITICAL
    MINLEVEL = NOTSET

    # dict to convert logging level back to symbolic name
    _level_num_to_name = {
                          NOTSET: 'NOTSET',
                          DEBUG: 'DEBUG',
                          INFO: 'INFO',
                          WARN: 'WARN',
                          ERROR: 'ERROR',
                          CRITICAL: 'CRITICAL',
                         }

    # dict to convert symbolic name to logging level
    # just invert _level_num_to_name
    _name_to_level_num = {value:key for (key, value) in _level_num_to_name.items()}

    # default maximum length of filename (enforced)
    DefaultMaxFname = 15


    def __init__(self, logfile=None, level=NOTSET, append=False,
                 max_fname=DefaultMaxFname):
        """Initialise the logging object.

        logfile  the path to the log file
        level    logging level - don't log below this level
        append   True if log file is appended to
        """

        # make sure we have same state as all other log objects
        self.__dict__ = Log.__shared_state

        # set some initial state
        self.max_fname = max_fname
        self.sym_level = 'NOTSET'      # set in call to check_level()
        self.level = self.check_level(level)

        # if not given logfile name, make one up
        if logfile is None:
            logfile = '%s.log' % __name__

        # get correct options for rewrite or append of logfile
        log_options = 'w'
        if append:
            log_options = 'a'

        # test if we can use the file
        try:
            self.logfd = open(logfile, log_options)
            self.logfd.close()
        except IOError:
            # assume we have readonly filesystem
            basefile = os.path.basename(logfile)
            if sys.platform == 'win32':
                logfile = os.path.join('C:\\', basefile)
            else:
                logfile = os.path.join('~', basefile)

        # try to open logfile again
        self.logfd = open(logfile, log_options)

        self.logfile = logfile

        # announce time+date of opening logging and logging level
        self.debug('='*55)
        self.debug('Log started on %s, log level=%s'
                   % (datetime.datetime.now().ctime(),
                      self._level_num_to_name[level]))
        self.debug('-'*55)

        # finally, set some internal state
        self.set_level(self.level)

    def check_level(self, level):
        """Check the level value for legality.

        level  a numeric logging level

        If 'level' is invalid, raise Exception.  If valid, return value.
        """

        try:
            level = int(level)
        except ValueError:
            msg = "Logging level invalid: '%s'" % str(level)
            print(msg)
            raise Exception(msg)

        if not self.NOTSET <= level <= self.CRITICAL:
            msg = "Logging level invalid: '%s'" % str(level)
            print(msg)
            raise Exception(msg)

        return level

    def set_level(self, level):
        """Set logging level."""

        level = self.check_level(level)

        # convert numeric level to symbolic
        sym = self._level_num_to_name.get(level, None)
        if sym is None:
            # not recognized symbolic but it's legal, so interpret as 'XXXX+2'
            sym_10 = 10 * (level/10)
            sym_rem = level - sym_10
            sym = '%s+%d' % (self._level_num_to_name[sym_10], sym_rem)

        self.level = level
        self.sym_level = sym

        self.critical('Logging level set to %02d (%s)' % (level, sym))

    def __call__(self, msg=None, level=None):
        """Call on the logging object.

        msg    message string to log
        level  level to log 'msg' at (if not given, assume self.level)
        """

        # get level to log at
        if level is None:
            level = self.level

        # are we going to log?
        if level < self.level or self.level < 0:
            return

        if msg is None:
            msg = ''

        # get time
        to = datetime.datetime.now()
        hr = to.hour
        min = to.minute
        sec = to.second
        msec = to.microsecond

        # caller information - look back for first module != <this module name>
        frames = traceback.extract_stack()
        frames.reverse()
        try:
            (_, mod_name) = __name__.rsplit('.', 1)
        except ValueError:
            mod_name = __name__
        for (fpath, lnum, mname, _) in frames:
            fname = os.path.basename(fpath).rsplit('.', 1)
            if len(fname) > 1:
                fname = fname[0]
            if fname != mod_name:
                break

        # get string for log level
        loglevel = self._level_num_to_name[level]

        fname = fname[:self.max_fname]
        self.logfd.write('%02d:%02d:%02d.%06d|%8s|%*s:%-4d|%s\n'
                         % (hr, min, sec, msec, loglevel, self.max_fname,
                            fname, lnum, msg))
        self.logfd.flush()

    def critical(self, msg):
        """Log a message at CRITICAL level."""

        self(msg, self.CRITICAL)

    def error(self, msg):
        """Log a message at ERROR level."""

        self(msg, self.ERROR)

    def warn(self, msg):
        """Log a message at WARN level."""

        self(msg, self.WARN)

    def info(self, msg):
        """Log a message at INFO level."""

        self(msg, self.INFO)

    def debug(self, msg):
        """Log a message at DEBUG level."""

        self(msg, self.DEBUG)

    def __del__(self):
        """Close the logging."""

        self.logfd.close()
        self.logfd = None


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
    import getopt

    global Quiet

    log = Log('nb.log', Log.DEBUG)

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

