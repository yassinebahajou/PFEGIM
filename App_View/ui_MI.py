# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mi.ui'
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
        MainWindow.resize(800, 600)
        self.actioncreate = QAction(MainWindow)
        self.actioncreate.setObjectName(u"actioncreate")
        self.actionimport = QAction(MainWindow)
        self.actionimport.setObjectName(u"actionimport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menufiles = QMenu(self.menubar)
        self.menufiles.setObjectName(u"menufiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufiles.menuAction())
        self.menufiles.addAction(self.actioncreate)
        self.menufiles.addAction(self.actionimport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncreate.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.actionimport.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.menufiles.setTitle(QCoreApplication.translate("MainWindow", u"files", None))
    # retranslateUi

