# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 382)
        self.Action_New_Recording = QAction(MainWindow)
        self.Action_New_Recording.setObjectName(u"Action_New_Recording")
        self.Action_Open_Recording = QAction(MainWindow)
        self.Action_Open_Recording.setObjectName(u"Action_Open_Recording")
        self.Action_Open_Folder = QAction(MainWindow)
        self.Action_Open_Folder.setObjectName(u"Action_Open_Folder")
        self.Action_Annotation = QAction(MainWindow)
        self.Action_Annotation.setObjectName(u"Action_Annotation")
        self.Action_Detect_Emotion = QAction(MainWindow)
        self.Action_Detect_Emotion.setObjectName(u"Action_Detect_Emotion")
        self.Action_Model_Training = QAction(MainWindow)
        self.Action_Model_Training.setObjectName(u"Action_Model_Training")
        self.Action_Model_Training_using_Keras = QAction(MainWindow)
        self.Action_Model_Training_using_Keras.setObjectName(u"Action_Model_Training_using_Keras")
        self.Action_Emotion_Detection_using_Keras = QAction(MainWindow)
        self.Action_Emotion_Detection_using_Keras.setObjectName(u"Action_Emotion_Detection_using_Keras")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.Action_Model_Training_using_Keras)
        self.menufile.addAction(self.Action_Emotion_Detection_using_Keras)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Action_New_Recording.setText(QCoreApplication.translate("MainWindow", u"New Recording", None))
        self.Action_Open_Recording.setText(QCoreApplication.translate("MainWindow", u"Open Recording", None))
        self.Action_Open_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.Action_Annotation.setText(QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.Action_Detect_Emotion.setText(QCoreApplication.translate("MainWindow", u"Detect Emotion using Sklearn", None))
        self.Action_Model_Training.setText(QCoreApplication.translate("MainWindow", u"Create Model using Sklearn", None))
        self.Action_Model_Training_using_Keras.setText(QCoreApplication.translate("MainWindow", u"Create Model", None))
        self.Action_Emotion_Detection_using_Keras.setText(QCoreApplication.translate("MainWindow", u"Detect Disease", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

