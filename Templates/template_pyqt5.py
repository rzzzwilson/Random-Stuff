#!/usr/bin/env python3

"""
A template for a PyQt5 program.

Usage: template_pyqt5.py [-d <number>] [-h]

Where -d <number>  sets the debug level
      -h           prints this help AND THEN STOPS
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QToolTip, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


# name and version number of the template
TemplateName = 'PyQt5 Template'
TemplateVersion = '0.1'

# width and height of top-level widget
WidgetWidth = 250
WidgetHeight = 150


class Template(QWidget):

    def __init__(self, debug):
        super().__init__()
        self.initUI(debug)

    def initUI(self, debug):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        label = QLabel('debug = %s' % str(debug), self)
        label.setFixedWidth(WidgetWidth)
        label.setAlignment(Qt.AlignCenter)
        self.setGeometry(300, 300, WidgetWidth, WidgetHeight)
        self.setWindowTitle('%s %s' % (TemplateName, TemplateVersion))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


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
        tkinter_error(msg)

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

    app = QApplication(args)
    ex = Template(debug)
    sys.exit(app.exec_())
