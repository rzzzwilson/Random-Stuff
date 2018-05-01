#!/usr/bin/env python3

"""
Code investigating:

https://www.reddit.com/r/learnpython/comments/7vh5k4/pyqt5_crashes_on_qlistidget_currentitemchanged/
"""

from PyQt5.QtWidgets import QWidget, QListWidget, QApplication


class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.list = QListWidget(self)
        for s in ['alpha', 'beta', 'gamma']:
            self.list.addItem(s)
        self.list.currentItemChanged.connect(self.updateMe)
        self.setGeometry(300, 300, 200, 100)
        self.show()

#    def updateMe(self, item):
#        print(item.text())

    def updateMe(self, curr, prev):
        if prev:
            print(f'curr={curr.text()}, prev={prev.text()}')
        else:
            print(f'curr={curr.text()}, prev=None')



app = QApplication([])
ex = Template()
app.exec_()
