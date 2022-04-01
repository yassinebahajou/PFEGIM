import os
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QPlainTextEdit, QMessageBox, QVBoxLayout, \
    QLabel
from PySide2 import QtCore
from App_View.ui_Detect_Disease_Window import Ui_Detect_Disease_Window, QPixmap
import matplotlib.pyplot as plt
from xml.dom import minidom
from xml.etree import ElementTree

from App_Controller.Detect_Disease_Controller import Detect_Disease_Controller


class Detect_Disease_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Detect_Disease_Window, self).__init__(parent=parent)
        self.ui = Ui_Detect_Disease_Window()
        self.ui.setupUi(self)
        self.setWindowTitle("Detect Disease")
        self.controller = Detect_Disease_Controller()
        # self.ui.button_remove_noise.setVisible(False)
        # self.ui.button_plot_features.setVisible(False)
        self.ui.button_browse_audio.clicked.connect(self.import_image_file)
        self.ui.button_play_audio.clicked.connect(self.play_audio)
        self.ui.button_plot_audio.clicked.connect(self.plot_audio)
        # self.ui.button_extract_features.clicked.connect(self.save_feature_csv)
        # self.ui.button_remove_noise.clicked.connect(self.remove_noise)
        # self.ui.button_show_features.clicked.connect(self.launchExcelFile)
        # self.ui.button_plot_features.clicked.connect(self.plot_features)
        self.ui.button_import_model.clicked.connect(self.import_model)
        self.ui.button_detect_emotion.clicked.connect(self.detect_emotion)


    def import_image_file(self):
        selected_Qurl = QFileDialog.getOpenFileUrl(self, "Choose XRAY to Import", 'D:', "Image Files (*.png )")[0]
        lay = QVBoxLayout(self.ui.widget)
        label = QLabel(self)
        pixmap = QPixmap(selected_Qurl.path()[1:])
        label.setPixmap(pixmap)
        self.ui.widget.resize(pixmap.width(),pixmap.height())
        self.resize(pixmap.width(),self.height()+pixmap.height())
        lay.addWidget(label)
        self.ui.button_play_audio.setEnabled(True)
        self.ui.button_plot_audio.setEnabled(True)
        # self.ui.button_extract_features.setEnabled(True)
        self.ui.progress_bar.setText("wave file selected.")

    def play_audio(self):
        self.ui.progress_bar.setText("audio playing now.")
        print("audio playing now.")
        self.controller.play_audio()
        self.ui.progress_bar.setText("audio playing end.")
        print("audio playing end. ")

    def plot_audio(self):
        self.ui.progress_bar.setText("plotting now.")
        print("plotting now. ")
        self.controller.plot_audio()
        self.ui.progress_bar.setText("plotting done.")
        print("plotting done. ")

    def import_model(self):
        print("import model")
        model_path =  str(QFileDialog.getOpenFileName(self, "get_path_solution", "/my_models", "Json Files (*.json)")[0])
        if model_path:
            # self.Databasefile.setText(fileName[0])

            #   If Windows, change the separator
            if os.sep == '/':
                model_path = model_path.replace('/', '\\')

        au, date_ = self.controller.import_model(model_path)
        self.show_msg_box("Model Imported successfully, The Model's accuracy is "+au+"%.")
        self.ui.label_model_details.setText("Auccuracy: "+au+", Date: "+date_)
        # print(self.controller.detect_emotion())

    def detect_emotion(self):
        emotion = self.controller.detect_emotion()
        self.show_msg_box("Emotion Detection Done,Emotions Detected "+emotion.upper()+" .")

    def show_msg_box(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec()

    def save_feature_csv(self):
        self.controller.extract_features()
        self.show_msg_box("Features Extracted Successfully")
        self.ui.button_detect_emotion.setEnabled(True)



    def plot_features(self):
        mfc, chrom, meli, mfccs_time, chroma_time, mels_time = self.extract_feature(self)
        plt.subplot(3, 1, 1)
        plt.title("mfccs")
        plt.plot(mfccs_time, mfc)
        plt.subplot(3, 1, 2)
        plt.title("chroma")
        plt.plot(chroma_time, chrom)
        plt.subplot(3, 1, 3)
        plt.title("mels")
        plt.plot(mels_time, meli)
        plt.show()


    # def remove_noise(self):
    #     (Frequency, array) = read(self.file_path)  # Reading the sound file.
    #     print(len(array))  # length of our array
    #     FourierTransformation = sp.fft.fft(array)  # Calculating the fourier transformation of the signal
    #     scale = np.linspace(0, Frequency, len(array))
    #     GuassianNoise = np.random.rand(len(FourierTransformation))  # Adding guassian Noise to the signal.
    #     NewSound = GuassianNoise + array
    #     write("audio_files/New-"+self.song_l_name+"-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound)  # Saving it to the file.
    #     b, a = signal.butter(5, 1000 / (Frequency / 2), btype='highpass')  # ButterWorth filter 4350
    #     filteredSignal = signal.lfilter(b, a, NewSound)
    #     c, d = signal.butter(5, 380 / (Frequency / 2), btype='lowpass')  # ButterWorth low-filter
    #     newFilteredSignal = signal.lfilter(c, d, filteredSignal)  # Applying the filter to the signal
    #     write("audio_files/New-Filtered-"+self.song_l_name+"-Sound.wav", Frequency, newFilteredSignal)  # Saving it to the file.
    #     self.file_path = "audio_files/New-Filtered-"+self.song_l_name+"-Sound.wav"
    #     self.song_name = "New-Filtered-"+self.song_l_name+"-Sound.wav"
    #     self.song_l_name = "New-Filtered-"+self.song_l_name+"-Sound"

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Detect_Disease_Window()
    window.show()

    sys.exit(app.exec_())