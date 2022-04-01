import sys

from PySide2.QtGui import QPixmap, QTextCursor
from PySide2.QtCore import QObject, SIGNAL, Signal
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from App_View.ui_Load_Window import Ui_LoadWindow


class LoadWindow(QMainWindow):
    def __init__(self,parent=None):
        super(LoadWindow, self).__init__(parent=parent)
        self.ui = Ui_LoadWindow()
        self.ui.setupUi(self)
        sys.stdout = EmittingStream()
        # self.connect(sys.stdout, Signal('textWritten(QString)'), self.write2Console)
        sys.stdout.textWritten.connect(self.normalOutputWritten)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()


class EmittingStream(QObject):

    textWritten = Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoadWindow()
    window.show()
    for i in range(0,100):
        print("halala",i)
    sys.exit(app.exec_())
