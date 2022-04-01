# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LoadWindow(object):
    def setupUi(self, LoadWindow):
        if not LoadWindow.objectName():
            LoadWindow.setObjectName(u"LoadWindow")
        LoadWindow.resize(600, 259)
        self.verticalLayoutWidget = QWidget(LoadWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(LoadWindow)

        QMetaObject.connectSlotsByName(LoadWindow)
    # setupUi

    def retranslateUi(self, LoadWindow):
        LoadWindow.setWindowTitle(QCoreApplication.translate("LoadWindow", u"Form", None))
        self.label.setText("")
    # retranslateUi

