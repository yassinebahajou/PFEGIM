# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 146)
        self.verticalLayout_2 = QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lineEdit_mail = QLineEdit(Login)
        self.lineEdit_mail.setObjectName(u"lineEdit_mail")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_mail)

        self.lineEdit_pwd = QLineEdit(Login)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_pwd)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_Login = QPushButton(Login)
        self.btn_Login.setObjectName(u"btn_Login")

        self.verticalLayout_3.addWidget(self.btn_Login)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"E-mail", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Mot de passe", None))
        self.btn_Login.setText(QCoreApplication.translate("Login", u"Connexion", None))
    # retranslateUi

