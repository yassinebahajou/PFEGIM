import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QApplication, QStackedWidget, QPushButton, QWidget, QLayout
from functools import partial
from App_Model.user import User
from App_View.addUser import AddUser
from App_View.ui_ManageUsers import Ui_dialog
from App_Controller.User_Controller import User_Controller




class ManageUsers(QDialog):
    def __init__(self,parent=None):
        super(ManageUsers, self).__init__(parent=parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.widget = QStackedWidget()
        self.loadListUsers()
        self.ui.btnNewUser.clicked.connect(self.redirectAddUser)

    def loadListUsers(self):
        self.controller = User_Controller()
        row = 0
        self.ui.TableSensors.setRowCount(len(self.controller.users))
        self.buttons = []
        for user in self.controller.users :
            print("loading... "+user.mail)
            self.ui.TableSensors.setItem(row,0, QtWidgets.QTableWidgetItem(str(row)))
            self.ui.TableSensors.setItem(row, 1, QtWidgets.QTableWidgetItem(user.mail))
            self.ui.TableSensors.setItem(row, 2, QtWidgets.QTableWidgetItem(user.pwd))
            self.ui.TableSensors.setItem(row, 3, QtWidgets.QTableWidgetItem(user.name))
            self.ui.TableSensors.setItem(row, 4, QtWidgets.QTableWidgetItem(user.isAdmin))
            # pWidget = QWidget()
            # pLayout = QLayout()
            button = QPushButton(self.ui.widget)
            button.setText("Delete User")
            button.clicked.connect(partial(self.delete_user,row))
            # pLayout.addWidget(button)
            # pWidget.setLayout(pLayout)
            self.ui.TableSensors.setCellWidget(row, 5,button)
            self.buttons.append(button)
            row = row+1

    def delete_user(self,user):
        # row = self.buttons.index(self)
        print(f"delete:{user}")
        self.controller.remove(user)
        self.loadListUsers()

    def redirectAddUser(self):
        sensor = AddUser(parent=self)
        sensor.show()








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ManageUsers()
    window.show()

    sys.exit(app.exec_())

