import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from App_View.ui_MainWindow import Ui_MainWindow
from App_View.Detect_Disease_Window import Detect_Disease_Window
from App_View.Train_Model_Window import Train_Model_Sklearn_Window,Train_Model_Keras_Window


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        lay = QVBoxLayout(self.ui.centralwidget)
        label = QLabel(self)
        pixmap = QPixmap('interfaces/image_1.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        lay.addWidget(label)
        # self.ui.Action_Detect_Emotion.triggered.connect(self.load_Detect_Emotion_Sklearn_Window)
        # self.ui.Action_Model_Training.triggered.connect(self.load_Train_Model_Sklearn_Window)
        self.ui.Action_Emotion_Detection_using_Keras.triggered.connect(self.load_Detect_Emotion_Keras_Window)
        self.ui.Action_Model_Training_using_Keras.triggered.connect(self.load_Train_Model_Keras_Window)



    # def load_Detect_Emotion_Sklearn_Window(self):
    #     Detect_Emotion_Dialog = Detect_Disease_Window(parent=self)
    #     Detect_Emotion_Dialog.show()
    #
    # def load_Train_Model_Sklearn_Window(self):
    #     Train_Model_Dialog = Train_Model_Sklearn_Window(parent=self)
    #     Train_Model_Dialog.show()

    def load_Detect_Emotion_Keras_Window(self):
        Detect_Emotion_Dialog = Detect_Disease_Window(parent=self)
        Detect_Emotion_Dialog.show()

    def load_Train_Model_Keras_Window(self):
        Train_Model_Dialog = Train_Model_Keras_Window(parent=self)
        Train_Model_Dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("skqcgfisec")
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
