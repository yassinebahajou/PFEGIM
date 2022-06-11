# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Train_Disease_Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Train_Model_Window(object):
    def setupUi(self, Train_Model_Window):
        if not Train_Model_Window.objectName():
            Train_Model_Window.setObjectName(u"Train_Model_Window")
        Train_Model_Window.resize(331, 171)
        self.formWidget = QWidget(Train_Model_Window)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(9, 9, 307, 137))
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.button_browse_directory = QPushButton(self.formWidget)
        self.button_browse_directory.setObjectName(u"button_browse_directory")
        self.button_browse_directory.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.button_browse_directory)

        self.combo_select = QComboBox(self.formWidget)
        self.combo_select.addItem("")
        self.combo_select.addItem("")
        self.combo_select.setObjectName(u"combo_select")
        self.combo_select.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.combo_select)

        self.line = QFrame(self.formWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(150, 0))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.line)

        self.button_load_data = QPushButton(self.formWidget)
        self.button_load_data.setObjectName(u"button_load_data")
        self.button_load_data.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.button_load_data)

        self.edit_audio_name = QLineEdit(self.formWidget)
        self.edit_audio_name.setObjectName(u"edit_audio_name")
        self.edit_audio_name.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_audio_name)

        self.button_init_model = QPushButton(self.formWidget)
        self.button_init_model.setObjectName(u"button_init_model")
        self.button_init_model.setEnabled(False)
        self.button_init_model.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_init_model)

        self.button_show_matrics = QPushButton(self.formWidget)
        self.button_show_matrics.setObjectName(u"button_show_matrics")
        self.button_show_matrics.setEnabled(False)
        self.button_show_matrics.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.button_show_matrics)

        self.progress_bar = QLabel(self.formWidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.progress_bar)

        self.widget = QWidget(Train_Model_Window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 152, 16, 16))

        self.retranslateUi(Train_Model_Window)

        QMetaObject.connectSlotsByName(Train_Model_Window)
    # setupUi

    def retranslateUi(self, Train_Model_Window):
        Train_Model_Window.setWindowTitle(QCoreApplication.translate("Train_Model_Window", u"Ui_Model_Tranining_Window", None))
        self.button_browse_directory.setText(QCoreApplication.translate("Train_Model_Window", u"Sélectionner un dossier", None))
        self.combo_select.setItemText(0, QCoreApplication.translate("Train_Model_Window", u"PNEUMONIA", None))
        self.combo_select.setItemText(1, QCoreApplication.translate("Train_Model_Window", u"Covid 19", None))

        self.button_load_data.setText(QCoreApplication.translate("Train_Model_Window", u"Importer Data", None))
        self.button_init_model.setText(QCoreApplication.translate("Train_Model_Window", u"Init Data", None))
        self.button_show_matrics.setText(QCoreApplication.translate("Train_Model_Window", u"Confusion Matrice", None))
        self.progress_bar.setText(QCoreApplication.translate("Train_Model_Window", u"sélectionner Xray Image.", None))
    # retranslateUi

