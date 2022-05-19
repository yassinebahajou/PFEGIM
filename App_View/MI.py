from PySide2.QtWidgets import QMainWindow

from ui_MI import Ui_MainWindow


class MI(QMainWindow):
    def __init__(self,parent=None):
        super(MI,self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actioncreate.trigged.connect(self.lala)
        


