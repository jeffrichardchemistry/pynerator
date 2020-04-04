# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(204, 272)
        MainWindow.setMinimumSize(QtCore.QSize(204, 272))
        MainWindow.setMaximumSize(QtCore.QSize(204, 272))
        MainWindow.setStyleSheet("background-color: rgba(85, 87, 83,0.6);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 150, 181, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_generate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_generate.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(186, 189, 182);")
        self.btn_generate.setObjectName("btn_generate")
        self.gridLayout.addWidget(self.btn_generate, 5, 0, 1, 1)
        self.txt_password = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txt_password.setStyleSheet("font: 11pt \"Open Sans\";")
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 6, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 188, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chkbox_number = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkbox_number.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(85, 87, 83);\n"
"")
        self.chkbox_number.setObjectName("chkbox_number")
        self.gridLayout_2.addWidget(self.chkbox_number, 1, 0, 1, 1)
        self.spinBox_specialchar = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_specialchar.setStyleSheet("color: rgb(186, 189, 182);")
        self.spinBox_specialchar.setObjectName("spinBox_specialchar")
        self.gridLayout_2.addWidget(self.spinBox_specialchar, 2, 1, 1, 1)
        self.chkbox_uppercase = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkbox_uppercase.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(85, 87, 83);\n"
"")
        self.chkbox_uppercase.setObjectName("chkbox_uppercase")
        self.gridLayout_2.addWidget(self.chkbox_uppercase, 3, 0, 1, 1)
        self.spinBox_uppercase = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_uppercase.setStyleSheet("color: rgb(186, 189, 182);")
        self.spinBox_uppercase.setObjectName("spinBox_uppercase")
        self.gridLayout_2.addWidget(self.spinBox_uppercase, 3, 1, 1, 1)
        self.chkbox_specialchar = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkbox_specialchar.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(85, 87, 83);\n"
"")
        self.chkbox_specialchar.setObjectName("chkbox_specialchar")
        self.gridLayout_2.addWidget(self.chkbox_specialchar, 2, 0, 1, 1)
        self.chkbox_character = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkbox_character.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(186, 189, 182);")
        self.chkbox_character.setObjectName("chkbox_character")
        self.gridLayout_2.addWidget(self.chkbox_character, 0, 0, 1, 1)
        self.spinBox_number = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_number.setStyleSheet("color: rgb(186, 189, 182);")
        self.spinBox_number.setObjectName("spinBox_number")
        self.gridLayout_2.addWidget(self.spinBox_number, 1, 1, 1, 1)
        self.spinBox_character = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_character.setStyleSheet("color: rgb(186, 189, 182);")
        self.spinBox_character.setObjectName("spinBox_character")
        self.gridLayout_2.addWidget(self.spinBox_character, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pynerator"))
        self.btn_generate.setText(_translate("MainWindow", "Generate"))
        self.txt_password.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Passwords...</span></p></body></html>"))
        self.chkbox_number.setText(_translate("MainWindow", "Numbers"))
        self.chkbox_uppercase.setText(_translate("MainWindow", "Uppercase"))
        self.chkbox_specialchar.setText(_translate("MainWindow", "Special Characters"))
        self.chkbox_character.setText(_translate("MainWindow", "Characters"))
