import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QApplication, QStackedWidget, QPushButton, QWidget, QLayout
from functools import partial
from App_Model.patient import Patient
from App_View.addUser import AddUser
from App_View.ui_ManagePatients import Ui_dialog
from App_Controller.Patient_Controller import Patient_Controller




class ManagePatient(QDialog):
    def __init__(self,parent=None):
        super(ManagePatient, self).__init__(parent=parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.widget = QStackedWidget()
        self.loadListUsers()
        print("manage patient here")

    def loadListUsers(self):
        self.controller = Patient_Controller()
        row = 0
        self.ui.TableSensors.setRowCount(len(self.controller.patients))
        self.buttons = []
        for patient in self.controller.patients :
            print("loading... "+patient.nom)
            self.ui.TableSensors.setItem(row,0, QtWidgets.QTableWidgetItem(str(row)))
            self.ui.TableSensors.setItem(row, 1, QtWidgets.QTableWidgetItem(patient.nom))
            self.ui.TableSensors.setItem(row, 2, QtWidgets.QTableWidgetItem(patient.prenom))
            self.ui.TableSensors.setItem(row, 3, QtWidgets.QTableWidgetItem(patient.age))
            self.ui.TableSensors.setItem(row, 4, QtWidgets.QTableWidgetItem(patient.sex))
            self.ui.TableSensors.setItem(row, 5, QtWidgets.QTableWidgetItem(patient.infected))
            # pWidget = QWidget()
            # pLayout = QLayout()
            button = QPushButton(self.ui.widget)
            button.setText("Afficher Image")
            button.clicked.connect(partial(self.plot_image,row))
            # pLayout.addWidget(button)
            # pWidget.setLayout(pLayout)
            self.ui.TableSensors.setCellWidget(row, 6,button)
            self.buttons.append(button)
            row = row+1

    def plot_image(self,patient_row):
        var = self.controller.patients[patient_row].xray_image
        img = mpimg.imread('files/xrayImages/'+var)
        plt.imshow(img)
        plt.show()


    def redirectAddUser(self):
        sensor = AddUser(parent=self)
        sensor.show()








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ManagePatient()
    window.show()

    sys.exit(app.exec_())

