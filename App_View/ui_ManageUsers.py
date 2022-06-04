# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Manage_Users.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(655, 445)
        dialog.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list = QLabel(self.widget)
        self.list.setObjectName(u"list")
        self.list.setStyleSheet(u"font: 11pt \"Andalus\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 75 italic 16pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.list)

        self.btnNewUser = QPushButton(self.widget)
        self.btnNewUser.setObjectName(u"btnNewUser")
        self.btnNewUser.setStyleSheet(u"font: 12pt \"MS UI Gothic\";\n"
"background-color: rgb(195, 193, 255);\n"
"")

        self.verticalLayout.addWidget(self.btnNewUser)

        self.TableSensors = QTableWidget(self.widget)
        if (self.TableSensors.columnCount() < 6):
            self.TableSensors.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableSensors.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.TableSensors.setObjectName(u"TableSensors")
        self.TableSensors.setStyleSheet(u"\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout.addWidget(self.TableSensors)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Manage Users", None))
        self.list.setText(QCoreApplication.translate("dialog", u"List Users", None))
        self.btnNewUser.setText(QCoreApplication.translate("dialog", u"Add New User", None))
        ___qtablewidgetitem = self.TableSensors.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dialog", u"Id", None));
        ___qtablewidgetitem1 = self.TableSensors.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dialog", u"Email", None));
        ___qtablewidgetitem2 = self.TableSensors.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dialog", u"Password", None));
        ___qtablewidgetitem3 = self.TableSensors.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dialog", u"Name", None));
        ___qtablewidgetitem4 = self.TableSensors.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dialog", u"IsAdmin", None));
        ___qtablewidgetitem5 = self.TableSensors.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dialog", u"Actions", None));
    # retranslateUi

