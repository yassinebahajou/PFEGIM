# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_User.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddUser(object):
    def setupUi(self, AddUser):
        if not AddUser.objectName():
            AddUser.setObjectName(u"AddUser")
        AddUser.resize(303, 267)
        self.formLayout = QFormLayout(AddUser)
        self.formLayout.setObjectName(u"formLayout")
        self.sensor = QFormLayout()
        self.sensor.setObjectName(u"sensor")
        self.sensor.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.sensor.setLabelAlignment(Qt.AlignCenter)
        self.sensor.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.sensor.setHorizontalSpacing(0)
        self.sensor.setVerticalSpacing(10)
        self.sensor.setContentsMargins(20, 10, 30, 10)
        self.TitleForm = QLabel(AddUser)
        self.TitleForm.setObjectName(u"TitleForm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleForm.sizePolicy().hasHeightForWidth())
        self.TitleForm.setSizePolicy(sizePolicy)
        self.TitleForm.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TitleForm.setFont(font)
        self.TitleForm.setLayoutDirection(Qt.LeftToRight)
        self.TitleForm.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")
        self.TitleForm.setAlignment(Qt.AlignCenter)
        self.TitleForm.setMargin(10)

        self.sensor.setWidget(0, QFormLayout.LabelRole, self.TitleForm)

        self.oid = QLabel(AddUser)
        self.oid.setObjectName(u"oid")
        self.oid.setStyleSheet(u"\n"
"font: 75 11pt \"Times New Roman\";")

        self.sensor.setWidget(1, QFormLayout.LabelRole, self.oid)

        self.le_name = QLineEdit(AddUser)
        self.le_name.setObjectName(u"le_name")

        self.sensor.setWidget(1, QFormLayout.FieldRole, self.le_name)

        self.name = QLabel(AddUser)
        self.name.setObjectName(u"name")

        self.sensor.setWidget(2, QFormLayout.LabelRole, self.name)

        self.le_mail = QLineEdit(AddUser)
        self.le_mail.setObjectName(u"le_mail")

        self.sensor.setWidget(2, QFormLayout.FieldRole, self.le_mail)

        self.maxValue = QLabel(AddUser)
        self.maxValue.setObjectName(u"maxValue")

        self.sensor.setWidget(3, QFormLayout.LabelRole, self.maxValue)

        self.le_pwd = QLineEdit(AddUser)
        self.le_pwd.setObjectName(u"le_pwd")

        self.sensor.setWidget(3, QFormLayout.FieldRole, self.le_pwd)

        self.minValue = QLabel(AddUser)
        self.minValue.setObjectName(u"minValue")

        self.sensor.setWidget(4, QFormLayout.LabelRole, self.minValue)

        self.le_repwd = QLineEdit(AddUser)
        self.le_repwd.setObjectName(u"le_repwd")

        self.sensor.setWidget(4, QFormLayout.FieldRole, self.le_repwd)

        self.Color = QLabel(AddUser)
        self.Color.setObjectName(u"Color")

        self.sensor.setWidget(5, QFormLayout.LabelRole, self.Color)

        self.BtnAddSensor = QPushButton(AddUser)
        self.BtnAddSensor.setObjectName(u"BtnAddSensor")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.BtnAddSensor.setFont(font1)

        self.sensor.setWidget(6, QFormLayout.FieldRole, self.BtnAddSensor)

        self.cb_role = QComboBox(AddUser)
        self.cb_role.addItem("")
        self.cb_role.addItem("")
        self.cb_role.setObjectName(u"cb_role")

        self.sensor.setWidget(5, QFormLayout.FieldRole, self.cb_role)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.sensor)


        self.retranslateUi(AddUser)

        QMetaObject.connectSlotsByName(AddUser)
    # setupUi

    def retranslateUi(self, AddUser):
        AddUser.setWindowTitle(QCoreApplication.translate("AddUser", u"Dialog", None))
        self.TitleForm.setText(QCoreApplication.translate("AddUser", u"Add User", None))
        self.oid.setText(QCoreApplication.translate("AddUser", u"Name: ", None))
        self.name.setText(QCoreApplication.translate("AddUser", u"Email:", None))
        self.maxValue.setText(QCoreApplication.translate("AddUser", u"Password:", None))
        self.minValue.setText(QCoreApplication.translate("AddUser", u"Re-Password", None))
        self.Color.setText(QCoreApplication.translate("AddUser", u"Role", None))
        self.BtnAddSensor.setText(QCoreApplication.translate("AddUser", u"Add", None))
        self.cb_role.setItemText(0, QCoreApplication.translate("AddUser", u"Admin", None))
        self.cb_role.setItemText(1, QCoreApplication.translate("AddUser", u"User", None))

    # retranslateUi

