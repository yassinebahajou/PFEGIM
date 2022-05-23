import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QApplication, QStackedWidget

from App_Model.user import User
from App_View.ui_ManageUsers import Ui_dialog
from App_Controller.Login_Controller import Login_Controller




class ManageUsers(QDialog):
    def __init__(self,parent=None):
        super(ManageUsers, self).__init__(parent=parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.widget = QStackedWidget()
        self.loadListUsers()
        #self.ui.btnNewSensor.clicked.connect(self.redirectAddSensor)

    def loadListUsers(self):
        self.controller = Login_Controller()
        row = 0
        for user in self.controller.users :
            print("loading... "+user.mail)
            self.ui.TableSensors.setItem(row,0, QtWidgets.QTableWidgetItem(str(row)))
            self.ui.TableSensors.setItem(row, 1, QtWidgets.QTableWidgetItem(user.mail))
            self.ui.TableSensors.setItem(row, 2, QtWidgets.QTableWidgetItem(user.pwd))
            self.ui.TableSensors.setItem(row, 3, QtWidgets.QTableWidgetItem(user.name))
            self.ui.TableSensors.setItem(row, 4, QtWidgets.QTableWidgetItem(user.isAdmin))
            row = row+1


    # def redirectAddSensor(self):
    #     sensor = AddSensor()
    #     self.widget.addWidget(sensor)
    #     self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    #     self.widget.show()








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ListSensors()
    window.show()

    sys.exit(app.exec_())

