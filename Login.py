import sys


from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from App_View.ui_Login import Ui_Login
from App_Controller.User_Controller import User_Controller
from MainWindow import MainWindow


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.btn_Login.clicked.connect(self.Login)
        self.controller = User_Controller()
        self.Current_User = None

    def Login(self):
        mail = self.ui.lineEdit_mail.text()
        password = self.ui.lineEdit_pwd.text()
        self.Current_User = self.controller.getUser(mail,password)
        if self.Current_User is not None:
            self.Open_MainWindow()
        else:
            self.show_msg_box("wrong email or password, please try again !!")


    def Open_MainWindow(self):
        Main_Window = MainWindow(parent=self)
        Main_Window.show()
        # Main_Window.maximumSize()
        self.hide()

    def show_msg_box(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("skqcgfisec")
    window = Login()
    window.show()
    sys.exit(app.exec_())
