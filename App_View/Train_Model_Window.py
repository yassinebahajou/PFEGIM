import os
import sys
import threading

from PySide2.QtCore import QThreadPool
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from App_Model.Worker import Worker
from App_View.ui_Train_Model_Window import Ui_Train_Model_Window
from App_View.Load_Window import LoadWindow
# from LoadingScreen import LoadingScreen
from App_Controller.Train_Model_Controller import Train_Model_Controller

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Train_Model_Keras_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Train_Model_Keras_Window, self).__init__(parent=parent)

        self.ui = Ui_Train_Model_Window()
        self.controller = Train_Model_Controller()
        self.ui.setupUi(self)
        self.setWindowTitle("Create Model Keras")
        self.threadpool = QThreadPool()
        self.ui.button_browse_directory.clicked.connect(self.GetDir)
        self.ui.button_load_data.clicked.connect(self.load_data_thread)
        self.ui.button_init_model.clicked.connect(self.init_model)
        self.ui.button_show_matrics.clicked.connect(self.show_matrics)
        # self.ui.button_save_model.clicked.connect(self.save_model)
        # self.load_screen = LoadingScreen()
        self.show()


    def GetDir(self):
        options = QFileDialog.DontUseNativeDialog
        self.fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory",'D:',
                            QFileDialog.ShowDirsOnly))
        if self.fileName:
            # self.Databasefile.setText(fileName[0])

            #   If Windows, change the separator
            if os.sep == '/':
                self.fileName = self.fileName.replace('/', '\\')
        # self.ui.edit_directory_name.setText(self.fileName)
        print(self.fileName)
        self.ui.button_load_data.setEnabled(True)


    def load_data(self):
        print('loading data')
        # wait = self.show_msg_box("Loading","Data is Loading, Please wait!!")
        self.controller.load_data(self.fileName)
        # wait.close()
        print('loading done')

    def load_data_thread(self):
        self.loading = LoadWindow(parent=self)
        self.loading.setWindowTitle("Loading Data")
        self.loading.ui.label.setText("Data is Loading, this might take a While Please Wait!!")
        # self.loading = LoadingScreen()
        self.loading.show()
        worker = Worker(self.load_data)  # Any other args, kwargs are passed to the run function
        worker.signals.finished.connect(self.load_data_complete)

        # Execute
        self.threadpool.start(worker)

    def load_data_complete(self):
        self.loading.close()
        self.loading.__del__()
        self.show_msg_box("Loading Done", "Data Loaded Successfully.")
        self.ui.button_init_model.setEnabled(True)

    def init_model(self):
        print('init model')
        self.controller.init_model(self.ui.combo_select.currentText())
        self.controller.train_model()
        self.init_model_complete()
        print( str(float("{:.2f}".format((self.controller.acc)))) + "%.")
        print('init done')

    def init_model_thread(self):
        self.loading = LoadWindow(parent=self)
        self.loading.show()
        worker = Worker(self.init_model)  # Any other args, kwargs are passed to the run function
        worker.signals.finished.connect(self.init_model_complete)

        # Execute
        self.threadpool.start(worker)


    def init_model_complete(self):
        # self.loading.close()
        self.show_msg_box("Init Done", "Model Initializing and Training done")
        self.show_msg_box("Init Done", "Model Initializing and Training done, The finale accuracy is " + str(
                        float("{:.2f}".format((self.controller.acc)))) + "%.")
        self.ui.button_init_model.setText("Re-Init Model")
        self.ui.button_show_matrics.setEnabled(True)
        self.ui.button_save_model.setEnabled(True)

    def save_model(self):
        print('save model')
        self.controller.save_model()
        self.show_msg_box("Save Done", "Model Was Saved Successefully")

        print('save done')

    def show_msg_box(self,title,text):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.exec()
        return  msgBox

    def show_matrics(self):
        # Setting the attributes
        fig, px = plt.subplots(figsize=(3.5, 3.5))
        px.matshow(self.controller.cm, cmap=plt.cm.YlOrRd, alpha=0.5)
        for m in range(self.controller.cm.shape[0]):
            for n in range(self.controller.cm.shape[1]):
                px.text(x=m, y=n, s=self.controller.cm[m, n], va='center', ha='center', size='xx-large')

        # Sets the labels
        plt.xlabel('Predictions', fontsize=16)
        plt.ylabel('Actuals', fontsize=16)
        plt.title('Confusion Matrix', fontsize=15)
        plt.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)

    # window = Train_Model_Keras_Window()
    window = Ui_Train_Model_Window()

    window.show()

    sys.exit(app.exec_())
