import sys
from PySide2.QtWidgets import QWidget, QApplication, QCheckBox, QDialog

from App_Controller.User_Controller import User_Controller
from App_Model.user import User
from App_View.ui_Add_User import Ui_AddUser



class AddUser(QDialog):
    def __init__(self, parent= None):
        super(AddUser,self).__init__(parent=parent)
        self.ui = Ui_AddUser()
        self.ui.setupUi(self)
        self.controller = User_Controller()
        self.ui.BtnAddSensor.clicked.connect(self.newUser)

    def newUser(self):
        name = self.ui.le_mail.text()
        email = self.ui.le_mail.text()
        pws = self.ui.le_pwd.text()
        repwd = self.ui.le_repwd.text()
        role = self.ui.cb_role.currentText()
        if role=="Admin":
            isAdmin = 1
        else :
            isAdmin = 0
        if pws == repwd:
            user = User(name=name,mail=email,pwd=pws,isAdmin=isAdmin)
            self.controller.add(user)
            self.parent().loadListUsers()
            self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AddUser()
    window.show()

    sys.exit(app.exec_())




