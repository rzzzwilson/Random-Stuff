#!/usr/bin/env python3

"""
Investigate catching exceptions in event handlers.
Applicable to GLib event loops?

Usage:  catch.py [catch]

where "catch" enables catching of exceptions.
"""

import sys
import random
import traceback
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class App(QWidget):
    def __init__(self):
        super().__init__()
        qbtn = QPushButton('Boom', self)
        qbtn.clicked.connect(self.boom)
        self.setGeometry(300, 300, 150, 50)
        self.show()

# to show that we can catch exceptions from explicit method calls, of course
#        # catch exception from explicit call to bad method
#        try:
#            self.boom()
#        except Exception as e:
#            print(f'Caught "{e}" exception from self.boom()')

    def boom(self):
        """Choose random exception."""

        exc_dict = {0: lambda : 2/0, 1: lambda : undefined(), 2: lambda : 1 + 'abc'}
        exc_dict[random.randrange(len(exc_dict))]()


# check the command line params
if len(sys.argv) == 2 and sys.argv[1].lower() == 'catch':
    # plug in our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)

    sys.excepthook = excepthook

app = QApplication([])
ex = App()
sys.exit(app.exec_())
