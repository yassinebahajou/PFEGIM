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
        Detect_Disease_Window.resize(415, 174)
        self.formWidget = QWidget(Detect_Disease_Window)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(0, 10, 411, 171))
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.button_import_model = QPushButton(self.formWidget)
        self.button_import_model.setObjectName(u"button_import_model")
        self.button_import_model.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.button_import_model)

        self.label_model_details = QLabel(self.formWidget)
        self.label_model_details.setObjectName(u"label_model_details")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_model_details)

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

        self.button_plot_audio = QPushButton(self.formWidget)
        self.button_plot_audio.setObjectName(u"button_plot_audio")
        self.button_plot_audio.setEnabled(False)
        self.button_plot_audio.setMinimumSize(QSize(150, 0))
        self.button_plot_audio.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.button_plot_audio)

        self.button_detect_emotion = QPushButton(self.formWidget)
        self.button_detect_emotion.setObjectName(u"button_detect_emotion")
        self.button_detect_emotion.setEnabled(False)
        self.button_detect_emotion.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.button_detect_emotion)

        self.progress_bar = QLabel(self.formWidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.progress_bar)

        self.widget = QWidget(Detect_Disease_Window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 180, 411, 161))

        self.retranslateUi(Detect_Disease_Window)

        QMetaObject.connectSlotsByName(Detect_Disease_Window)
    # setupUi

    def retranslateUi(self, Detect_Disease_Window):
        Detect_Disease_Window.setWindowTitle(QCoreApplication.translate("Detect_Disease_Window", u"Detect_Emotion_Window", None))
        self.button_import_model.setText(QCoreApplication.translate("Detect_Disease_Window", u"Import Model", None))
        self.label_model_details.setText("")
        self.button_browse_audio.setText(QCoreApplication.translate("Detect_Disease_Window", u"Browse XRay Image", None))
        self.button_play_audio.setText(QCoreApplication.translate("Detect_Disease_Window", u"Show Xray Image", None))
        self.button_plot_audio.setText(QCoreApplication.translate("Detect_Disease_Window", u"Plot Image", None))
        self.button_detect_emotion.setText(QCoreApplication.translate("Detect_Disease_Window", u"Detect Disease", None))
        self.progress_bar.setText(QCoreApplication.translate("Detect_Disease_Window", u"select you Xray Image.", None))
    # retranslateUi

