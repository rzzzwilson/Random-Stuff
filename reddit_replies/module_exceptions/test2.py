#!/usr/bin/env python3

"""
Investigate catching exceptions in event handlers.

Usage:  test.py [catch]

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

    def boom(self):
        2/0


app = QApplication([])
ex = App()
sys.exit(app.exec_())
