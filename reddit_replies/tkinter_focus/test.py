from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QToolTip, QLabel
from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


# name and version number of the template
ProgName = 'QPushButton In/Out Focus test'
ProgVersion = '0.1'

# width and height of top-level widget
WidgetWidth = 250
WidgetHeight = 150


class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def focusInEvent(self, ev):
        print('!!!!!')
        return QLineEdit.focusInEvent(self, ev)

class Test(QWidget):
    def __init__(self):
        super().__init__()
        qbtn = QPushButton('Press me', self)
        #qbtn = MyButton('Press me', self)
        qbtn.installEventFilter(self)
        qbtn.clicked.connect(self.pressed)
        qbtn.move(50, 50)
        self.setGeometry(300, 300, WidgetWidth, WidgetHeight)
        self.setWindowTitle('%s %s' % (ProgName, ProgVersion))
        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
                print("focusIn")
        return super(Test, self).eventFilter(obj, event)

    def focusIn(self, event):
        print('focusIn')

    def pressed(self, e):
        print('You pressed the button')


app = QApplication([])
ex = Test()
app.exec_()
