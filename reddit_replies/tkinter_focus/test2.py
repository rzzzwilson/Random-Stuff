from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.btn = QPushButton('Press me', self)
        self.btn.clicked.connect(self.pressed)
        self.btn.move(50, 50)
        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle('Focus event test')
        self.show()
        self.btn.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if obj == self.btn:
                self.btn.setStyleSheet("background-color: red")
        if event.type() == QEvent.Leave:
            if obj == self.btn:
                self.btn.setStyleSheet("background-color: white")
        return super(Widget, self).eventFilter(obj, event)

    def pressed(self, event):
        print('You pressed the button')


app = QApplication([])
w = Widget()
w.show()
app.exec_()
