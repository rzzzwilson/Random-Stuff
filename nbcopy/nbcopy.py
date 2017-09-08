#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A program to initialize a new NOTEBOOK USB stick from either:
    . an existing USB stick
    . an 'nb' backup directory

TODO: Implement a status line during formatting and copying.
      This requires a separate thread and signals back to
      the main (GUI) thread.
"""

import os
import sys
import shlex
import os.path as osp
import io
from subprocess import Popen, PIPE, STDOUT
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QToolTip, QLabel
from PyQt5.QtWidgets import QGridLayout, QComboBox, QCheckBox
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import logger

# name and version number of the template
ProgName = 'NBCopy'
ProgVersion = '2.1'

# width and height of top-level widget
MinimumWidth = 600

# string that allows user to select directory in filesystem
SelectDirString = 'Select directory or drive...'
SelectDestDrive = 'Select a destination drive'

# name of the .diskid file and actual notebook HTML file
IdFile = '.diskid'
IdFileString = 'NOTEBOOK\n'
NotebookFile = 'notebook.html'

# globals containing source paths
SourcePaths = []


def path_exists(path):
    """Decide if a given path exists."""

    log('path_exists: returning osp.isdir(%s)=%s' % (path, osp.isdir(path)))
    return osp.isdir(path)

def get_usb_drives():
    """Returns a list of filesystem paths to mounted USB drives."""

    result = []

    process = Popen(['system_profiler', 'SPUSBDataType'], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    output = output.decode("utf-8")

    for line in output.split('\n'):
        if 'Mount Point:' in line:
            (_, path) = line.split(':', 2)
            while path.startswith(' '):
                path = path[1:]
            result.append(path)

    return result


######
# A thread to perform a format/copy of the destination drive.
######

class CopyThread(QThread):
    """A thread to do the format/copy to a destination drive.

    It sends a signal to the main thread when finished.
    It also sends status signals to the main thread.
    """

    copy_done = pyqtSignal(str)
    status = pyqtSignal(str)

    def __init__(self, log, source, destination):
        """Create a thread to read one morse character.

        log          logging object
        source       path to the source drive/destination
        destination  path to the drive to process
        """

        super().__init__()
        self.log = log
        self.source = source
        self.destination = destination

    def exec_cmd(self, cmd):
        """Execute a shell command and return output and exit_code."""

        process = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        return (output, exit_code)

    def run(self):
        """Copy a source drive/directory to a destination drive."""

        # get list of current USB drives
        drives = get_usb_drives()

        # format the destination device
        self.status.emit('Erasing volume %s' % self.destination)
        self.log("Erasing volume on '%s'" % self.destination)
        cmd = 'diskutil eraseVolume FAT32 NOTEBOOK "%s"' % self.destination
        self.log('Command is: %s' % cmd)
        (output, exit_code) = self.exec_cmd(cmd)
        self.log('exit_code=%d' % exit_code)
        self.log('output:\n%s' % output)
        # check for errors

        # figure out path to newly formatted USB disk
        # drive that is in 'current' but NOT in 'self.drives' is the one
        current = get_usb_drives()
        self.log('current=%s' % str(current))
        new_drives = []
        for dev in current:
            self.log('checking dev=%s' % dev)
            if dev not in drives:
                new_drives.append(dev)
        if len(new_drives) != 1:
            # newly formatted drive has same name as before
            new_drives = [self.destination]
        new_destination = new_drives[0]
        drives = current

        # copy from source to deNONE,stination
        self.status.emit('Copying to volume %s' % new_destination)
        self.log("Copying '%s' to '%s'" % (self.source, new_destination))
        cmd = 'rsync --info=NONE,progress2 -r "%s"/* "%s"' % (self.source, new_destination)
        self.log('Command is: %s' % cmd)
        self.do_copy(cmd)
#        (output, exit_code) = self.exec_cmd(cmd)
#        self.log('exit_code=%d' % exit_code)
#        self.log('output:\n%s' % output)
        # check for errors

        # signal the main thread
        self.status.emit('Copy finished')
        self.copy_done.emit(new_destination)

    def do_copy(self, cmd):
        """Perform the copy, capturing output."""

        proc = Popen(cmd, shell=True, stdout=PIPE)
        stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')

        last_percent = None

        while True:
            output = stdout.readline().rstrip()
            #log("output='%s', last_percent=%s" % (output, str(last_percent)))
            if last_percent and output == '':
                log('Command finished')
                break
            if output == '':
                #log('ignoring blank line')
                continue
            #    111,225,882  13%    5.63MB/s
            percent = output.split()[1]
            if percent != last_percent:
                self.status.emit('Copy %s complete' % percent)
                last_percent = percent


#remainder = proc.communicate()[0].decode('utf-8')

class NBCopy(QWidget):

    def __init__(self, debug):
        super().__init__()

        # get all mounted drives
        self.drives = get_usb_drives()

        # set state variables
        self.debug = debug
        self.source = None
        self.destination = None

        self.initUI()

    def initUI(self):
        """Draw the UI."""

        QToolTip.setFont(QFont('SansSerif', 12))

        grid = QGridLayout()
        self.setLayout(grid)

        lbl_source = QLabel('Source:', self)
        lbl_source.setAlignment(Qt.AlignCenter)

        lbl_destination = QLabel('Destination:', self)
        lbl_destination.setAlignment(Qt.AlignCenter)

        self.cmb_source = QComboBox(self)
        self.populate_cmb_source()
        self.cmb_source.activated.connect(self.source_activated)
        self.cmb_source.setToolTip("Select either a source USB device "
                                   "or a source 'nb' backup directory")

        self.cmb_destination = QComboBox(self)
        self.populate_cmb_destination()
        self.cmb_destination.activated.connect(self.destination_activated)
        self.cmb_destination.setToolTip('Select a destination USB device')

        self.lbl_status = QLabel('', self)
        self.lbl_status.setAlignment(Qt.AlignLeft)
        self.btn_copy = QPushButton('Copy', self)
#        self.btn_copy.setFixedWidth(80)
        self.btn_copy.setFixedWidth(self.btn_copy.width())
        self.btn_copy.clicked.connect(self.start_copy)
        self.btn_copy.setEnabled(False)

        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl_status, Qt.AlignLeft)
        hbox.addStretch(1)
        hbox.addWidget(self.btn_copy, Qt.AlignRight)
        hbox.maximumSize()

        grid.addWidget(lbl_source, 0, 0, Qt.AlignRight)
        grid.addWidget(self.cmb_source, 0, 1)

        grid.addWidget(lbl_destination, 1, 0, Qt.AlignRight)
        grid.addWidget(self.cmb_destination, 1, 1)

        grid.addLayout(hbox, 2, 1)

        grid.setColumnStretch(0, 0)
        grid.setColumnStretch(1, 1)

        self.setWindowTitle('%s %s' % (ProgName, ProgVersion))
        self.setMinimumWidth(MinimumWidth)
        self.show()
        self.setFixedHeight(self.height())

    def populate_cmb_source(self):
        """Fill the source combobox with choices."""

        # remove current items
        while self.cmb_source.count():
            self.cmb_source.removeItem(0)

        # fill combobox with new items
        self.cmb_source.addItem(SelectDirString)
        for path in self.drives:
            self.cmb_source.addItem(path)
        for path in SourcePaths:
            self.cmb_source.addItem(path)

    def populate_cmb_destination(self):
        """Fill the destination combobox with choices."""

        # remove current items
        while self.cmb_destination.count():
            self.cmb_destination.removeItem(0)

        self.cmb_destination.addItem(SelectDestDrive)
        for path in self.drives:
            self.cmb_destination.addItem(path)

    def source_activated(self):
        """User chooses source device/directory."""

        # get source path from combobox
        source = self.cmb_source.currentText()

        if source == SelectDirString:
            # user wants to source from a directory, choose with a file dialog
            dirname = QFileDialog.getExistingDirectory(self, 'Select a source directory:',
                                                       osp.expanduser('~'),
                                                       QFileDialog.ShowDirsOnly)
            self.source = dirname
            if dirname not in SourcePaths:
                SourcePaths.append(dirname)
            self.populate_cmb_source()
            index = self.cmb_source.findText(dirname, Qt.MatchFixedString)
            if index >= 0:
                self.cmb_source.setCurrentIndex(index)
        else:
            self.source = source

        # check that source is good
        if self.source:
            if not self.good_source(self.source):
                self.warn("Path '%s' is a bad source" % self.source)
                self.source = None

        self.check_copy_disabled()

    def destination_activated(self):
        self.destination = self.cmb_destination.currentText()

        # check with user if destination correct
        if not self.good_destination(self.destination):
            self.warn("Path '%s' is a bad destination" % self.destination)
            self.destination = None

        index = self.cmb_destination.findText(self.destination, Qt.MatchFixedString)
        if index >= 0:
            self.cmb_destination.setCurrentIndex(index)

        self.check_copy_disabled()

    def start_copy(self):
        """Start the actual copy.

        Two threads do the formatting/copying, a control thread and a worker
        thread.  This function starts the control thread which manages the 
        worker thread.  The control thread signals this (GUI) thread with two
        message types:
            Status
            Finished
        """

        # disable the 'Copy' button while doing this
        self.btn_copy.setEnabled(False)

        # start the thread to do the work
        self.threadCopy = CopyThread(log, self.source, self.destination)
        self.threadCopy.copy_done.connect(self.copy_thread_finished)
        self.threadCopy.status.connect(self.copy_thread_status)
        self.threadCopy.start()
        log('Copy thread started')

    def copy_thread_status(self, status):
        """Receive a status signal from the copy thread."""

        log('Thread.status=%s' % status)
        self.lbl_status.setText(status)

    def copy_thread_finished(self, new_destination):
        log("Writing '%s' into file '%s'" % (IdFileString, osp.join(new_destination, IdFile)))
        with open(osp.join(new_destination, IdFile), 'w') as fd:
            fd.write(IdFileString)

        self.warn("Finished copying to\n'%s'." % new_destination)

        # reset comboboxes for another possible copy
        self.cmb_source.setCurrentIndex(0)
        self.cmb_destination.setCurrentIndex(0)

        # reset source & destination ready for next try
        # this enables the 'Copy' button
        self.source = None
        self.destination = None
        self.check_copy_disabled()

        # clear the status display
        self.lbl_status.setText('')

    def check_copy_disabled(self):
        """Copy button only enabled if both src&dest defined."""

        state = bool(self.source and self.destination)
        self.btn_copy.setEnabled(state)

    def good_source(self, source):
        """Check that a given source path is a valid source.
       
        This mainly consists of checking that the '.diskid' file exists
        in the root directory and gas the right contents.
        """

        # we need the .diskid file with correct contents
        diskid_file = osp.join(source, IdFile)
        if not osp.isfile(diskid_file):
            log('%s is not a file!?' % diskid_file)
            return False
        with open(diskid_file, 'r') as fd:
            line = fd.read()
        if line != IdFileString:
            log("File %s doesn't contain '%s' but '%s'" % (diskid_file, IdFileString, line))
            return False

        return True

    def good_destination(self, destination):
        """Check that a given destination path is a valid destination."""

        return True

    def exec_cmd(self, cmd):
        """Execute command and return output and exit code."""

#        args = shlex.split(cmd)
#        process = Popen(args, stdout=PIPE)
        process = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        return (output, exit_code)

    def warn(self, msg):
        log(msg)
        QMessageBox.information(self, '%s %s' % (ProgName, ProgVersion),
                                msg, QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        log('Exception caught:' + msg)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the program params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'd:h', ['debug=', 'help'])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(1)

    debug = 10              # no logging

    for (opt, param) in opts:
        if opt in ['-d', '--debug']:
            try:
                debug = int(param)
            except ValueError:
                usage("-d must be followed by an integer, got '%s'" % param)
                sys.exit(1)
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    log = logger.Log('nbcopy.log', debug)

    app = QApplication(args)
    ex = NBCopy(debug)
    sys.exit(app.exec_())
