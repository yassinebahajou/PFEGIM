# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Detect_Disease_Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Detect_Disease_Window(object):
    def setupUi(self, Detect_Disease_Window):
        if not Detect_Disease_Window.objectName():
            Detect_Disease_Window.setObjectName(u"Detect_Disease_Window")
        Detect_Disease_Window.resize(331, 171)
        self.formWidget = QWidget(Detect_Disease_Window)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(9, 9, 307, 137))
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.button_import_model = QPushButton(self.formWidget)
        self.button_import_model.setObjectName(u"button_import_model")
        self.button_import_model.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.button_import_model)

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

        self.button_browse_audio = QPushButton(self.formWidget)
        self.button_browse_audio.setObjectName(u"button_browse_audio")
        self.button_browse_audio.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.button_browse_audio)

        self.edit_audio_name = QLineEdit(self.formWidget)
        self.edit_audio_name.setObjectName(u"edit_audio_name")
        self.edit_audio_name.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_audio_name)

        self.button_play_audio = QPushButton(self.formWidget)
        self.button_play_audio.setObjectName(u"button_play_audio")
        self.button_play_audio.setEnabled(False)
        self.button_play_audio.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_play_audio)

        self.button_detect_emotion = QPushButton(self.formWidget)
        self.button_detect_emotion.setObjectName(u"button_detect_emotion")
        self.button_detect_emotion.setEnabled(False)
        self.button_detect_emotion.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.button_detect_emotion)

        self.progress_bar = QLabel(self.formWidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.progress_bar)

        self.widget = QWidget(Detect_Disease_Window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 152, 16, 16))

        self.retranslateUi(Detect_Disease_Window)

        QMetaObject.connectSlotsByName(Detect_Disease_Window)
    # setupUi

    def retranslateUi(self, Detect_Disease_Window):
        Detect_Disease_Window.setWindowTitle(QCoreApplication.translate("Detect_Disease_Window", u"Detect_Emotion_Window", None))
        self.button_import_model.setText(QCoreApplication.translate("Detect_Disease_Window", u"Importer un Modèle", None))
        self.combo_select.setItemText(0, QCoreApplication.translate("Detect_Disease_Window", u"PNEUMONIA", None))
        self.combo_select.setItemText(1, QCoreApplication.translate("Detect_Disease_Window", u"COVID-19", None))

        self.button_browse_audio.setText(QCoreApplication.translate("Detect_Disease_Window", u"Sélectionner une Image", None))
        self.button_play_audio.setText(QCoreApplication.translate("Detect_Disease_Window", u"Afficher l'Image", None))
        self.button_detect_emotion.setText(QCoreApplication.translate("Detect_Disease_Window", u"Résultat", None))
        self.progress_bar.setText(QCoreApplication.translate("Detect_Disease_Window", u"select you Xray Image.", None))
    # retranslateUi

