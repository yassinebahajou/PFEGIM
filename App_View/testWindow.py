import sys

from PySide2.QtWidgets import QMainWindow, QApplication
from ui_testWindow import Ui_MainWindow

class testwindow(QMainWindow):
    def __init__(self,parent=None):
        super(testwindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.p.clicked.connect(self.sayHello)


    def sayHello(selyf):
        print('hello')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = testwindow()
    window.show()

    sys.exit(app.exec_())