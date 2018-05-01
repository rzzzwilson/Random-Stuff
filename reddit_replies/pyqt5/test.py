import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
class WindowOne(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        b = QPushButton('Click me', self)
 
        b.clicked.connect(self.click)
 
        self.show()
 
    def click(self):
        self.w2 = WindowTwo()
 
 
class WindowTwo(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.show()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowOne()
    sys.exit(app.exec_())
