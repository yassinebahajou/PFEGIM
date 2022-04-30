import sys

from PySide2.QtWidgets import QMainWindow, QApplication
from ui_testtest import Ui_MainWindow

class testtest(QMainWindow):
    def __init__(self,parent=None):
        super(testtest, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sayHello)


    def sayHello(selyf):
        print('hello')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = testtest()
    window.show()

    sys.exit(app.exec_())