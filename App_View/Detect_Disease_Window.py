import os
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QPlainTextEdit, QMessageBox, QVBoxLayout, \
    QLabel
from PySide2 import QtCore
from App_View.ui_Detect_Disease_Window import Ui_Detect_Disease_Window, QPixmap
from keras.preprocessing import image
import numpy as np

from App_Controller.Detect_Disease_Controller import Detect_Disease_Controller
from App_View.addPatient import AddPatient


class Detect_Disease_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Detect_Disease_Window, self).__init__(parent=parent)
        self.ui = Ui_Detect_Disease_Window()
        self.ui.setupUi(self)
        self.setWindowTitle("Detect Disease")

        self.controller = Detect_Disease_Controller()
        self.ui.button_browse_audio.clicked.connect(self.import_image_file)
        self.ui.button_import_model.clicked.connect(self.import_model)
        self.ui.button_detect_emotion.setEnabled(True)
        self.ui.button_detect_emotion.clicked.connect(self.detect_disease)
        self.ui.button_save_patient.clicked.connect(self.AddPatientWindow)



    def import_image_file(self):
        selected_Qurl = QFileDialog.getOpenFileUrl(self, "Choose XRAY to Import", 'D:')[0]
        lay = QVBoxLayout(self.ui.imageWidget)
        label = QLabel(self)
        pixmap = QPixmap(selected_Qurl.path()[1:])
        label.setPixmap(pixmap)
        self.ui.imageWidget.resize(pixmap.width(),pixmap.height())
        self.ui.widget.resize(self.width(),self.height())
        # self.resize(pixmap.width(),self.height()+pixmap.height())
        lay.addWidget(label)
        self.ui.button_play_audio.setEnabled(True)
        # self.ui.button_extract_features.setEnabled(True)
        self.load_image(selected_Qurl.path()[1:])
        print("image url:",selected_Qurl.path()[1:])
        self.ui.progress_bar.setText("image sélectionnée.")

    def load_image(self,file_path):
        self.img_path = file_path
        self.img = image.load_img(file_path, target_size=(150, 150))
        self.img = image.img_to_array(self.img) / 255
        self.img = np.array([self.img])
        # self.save_image(file_path)
        print("image shape: ",self.img)
        print("image shape: ",self.img[0].shape)
        return self.img.shape


    def import_model(self):
        print("import model")
        # model_path =  str(QFileDialog.getOpenFileName(self, "get_path_solution", "/my_models", "Json Files (*.json)")[0])
        # if model_path:
        #     if os.sep == '/':
        #         model_path = model_path.replace('/', '\\')

        self.controller.import_model(self.ui.combo_select.currentText())
        self.ui.progress_bar.setText(self.ui.combo_select.currentText()+" modèle importé.")
        self.setWindowTitle("Detect Disease PNEUMONIA")
        # self.show_msg_box("Model Imported successfully, The Model's accuracy is "+au+"%.")
        # self.ui.label_model_details.setText("Auccuracy: "+au+", Date: "+date_)
        # print(self.controller.detect_emotion())

    def detect_disease(self):
        self.disease = self.controller.detect_disease(self.img)
        print("emotion:", self.disease)
        self.show_msg_box("Détection d'infection terminée ,X-Ray ["+self.disease+"]")
        # r1,r2 = self.controller.get_class_activation_map(self.img[0])
        # print(r1," tata ",type(r1))
        # print(r2," tata ",type(r2))

    def show_msg_box(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec()

    def save_feature_csv(self):
        self.controller.extract_features()
        self.show_msg_box("Features Extracted Successfully")
        self.ui.button_detect_emotion.setEnabled(True)

    def openFileDialog(self):
        # filename = QFileDialog.getOpenFileUrl(self,'open file')
        dialog = QDialog(self)
        dialog.setWindowTitle("File Features")
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # Add text field
        texterea = QPlainTextEdit(dialog)
        texterea.insertPlainText(self.current_file_features)
        texterea.move(10, 10)
        texterea.resize(400, 800)
        dialog.exec_()

    def launchExcelFile(self):
        os.system("start EXCEL.EXE "+self.current_file_features)

    def AddPatientWindow(self):
        window = AddPatient(Image=self.img_path,infected = self.disease+" "+self.ui.combo_select.currentText(),parent=self)
        window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Detect_Disease_Window()
    window.show()

    sys.exit(app.exec_())