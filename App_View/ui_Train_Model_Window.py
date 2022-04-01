# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Model_Training_Window.ui'
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


class Ui_Model_Tranining_Window(object):
    def setupUi(self, Model_Tranining_Window):
        if not Model_Tranining_Window.objectName():
            Model_Tranining_Window.setObjectName(u"Model_Tranining_Window")
        Model_Tranining_Window.resize(415, 338)
        self.formWidget = QWidget(Model_Tranining_Window)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(0, 10, 401, 311))
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.button_browse_directory = QPushButton(self.formWidget)
        self.button_browse_directory.setObjectName(u"button_browse_directory")
        self.button_browse_directory.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.button_browse_directory)

        self.edit_directory_name = QLineEdit(self.formWidget)
        self.edit_directory_name.setObjectName(u"edit_directory_name")
        self.edit_directory_name.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_directory_name)

        self.button_load_data = QPushButton(self.formWidget)
        self.button_load_data.setObjectName(u"button_load_data")
        self.button_load_data.setEnabled(False)
        self.button_load_data.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.button_load_data)

        self.button_init_model = QPushButton(self.formWidget)
        self.button_init_model.setObjectName(u"button_init_model")
        self.button_init_model.setEnabled(False)
        self.button_init_model.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.button_init_model)

        self.button_show_matrics = QPushButton(self.formWidget)
        self.button_show_matrics.setObjectName(u"button_show_matrics")
        self.button_show_matrics.setEnabled(False)
        self.button_show_matrics.setMinimumSize(QSize(150, 0))
        self.button_show_matrics.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_show_matrics)

        self.button_save_model = QPushButton(self.formWidget)
        self.button_save_model.setObjectName(u"button_save_model")
        self.button_save_model.setEnabled(False)
        self.button_save_model.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.button_save_model)

        self.progress_bar = QLabel(self.formWidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.progress_bar)


        self.retranslateUi(Model_Tranining_Window)

        QMetaObject.connectSlotsByName(Model_Tranining_Window)
    # setupUi

    def retranslateUi(self, Model_Tranining_Window):
        Model_Tranining_Window.setWindowTitle(QCoreApplication.translate("Model_Tranining_Window", u"Model_Taining_Window", None))
        self.button_browse_directory.setText(QCoreApplication.translate("Model_Tranining_Window", u"Browse Source", None))
        self.button_load_data.setText(QCoreApplication.translate("Model_Tranining_Window", u"Load Data", None))
        self.button_init_model.setText(QCoreApplication.translate("Model_Tranining_Window", u"Init Model", None))
        self.button_show_matrics.setText(QCoreApplication.translate("Model_Tranining_Window", u"Show Matrics", None))
        self.button_save_model.setText(QCoreApplication.translate("Model_Tranining_Window", u"Save Model", None))
        self.progress_bar.setText(QCoreApplication.translate("Model_Tranining_Window", u"select you wav file .", None))
    # retranslateUi

