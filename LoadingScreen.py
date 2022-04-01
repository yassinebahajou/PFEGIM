import sys

from PySide2.QtGui import QMovie
from PySide2.QtWidgets import QWidget, QLabel, QApplication

from PySide2.QtCore import Qt, QTimer


class LoadingScreen(QWidget):
    def __init__(self,):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie("C:/Users/Dell/Documents/Loading_2.gif")
        self.label_animation.setMovie(self.movie)

        # timer = QTimer(self)
        self.startAnimation()

        # timer.singleShot(3000,self.stopAnimation)

    def startAnimation(self):
        self.movie.start()
        self.show()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoadingScreen()
    # window.show()

    sys.exit(app.exec_())