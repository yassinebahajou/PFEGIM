import sys
from PySide2.QtWidgets import QWidget, QApplication, QCheckBox, QDialog

from App_Controller.Patient_Controller import Patient_Controller
from App_Model.patient import Patient
from App_View.ui_Add_Patient import Ui_AddUser
from keras.preprocessing.image import save_img,load_img,img_to_array



class AddPatient(QDialog):
    def __init__(self,Image,infected, parent= None):
        super(AddPatient,self).__init__(parent=parent)
        self.ui = Ui_AddUser()
        self.ui.setupUi(self)
        self.image = Image
        self.controller = Patient_Controller()
        self.filename = "xray"+str(len(self.controller.patients))+".jpg"
        self.infected = infected
        self.save_image(Image,self.filename)
        self.ui.BtnAdd.clicked.connect(self.newPatient)

    def newPatient(self):
        name = self.ui.le_name.text()
        prenom = self.ui.le_prenom.text()
        age = self.ui.le_age.text()
        sex = self.ui.cb_sex.currentText()
        xray = self.filename
        p = Patient(name,prenom,age,sex,self.infected,xray)
        self.controller.add(p)
        self.close()

    def save_image(self,file_path,filename):
        img = load_img(file_path, target_size=(150, 150))
        img = img_to_array(img)
        save_img('files/xrayImages/'+filename, img)
        return filename





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AddPatient()
    window.show()

    sys.exit(app.exec_())




