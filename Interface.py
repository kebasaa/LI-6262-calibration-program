# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 221)
        self.COM_LI6262 = QtWidgets.QComboBox(Dialog)
        self.COM_LI6262.setGeometry(QtCore.QRect(150, 10, 241, 22))
        self.COM_LI6262.setObjectName("COM_LI6262")
        self.CO2SpanVal = QtWidgets.QLineEdit(Dialog)
        self.CO2SpanVal.setGeometry(QtCore.QRect(270, 90, 51, 20))
        self.CO2SpanVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CO2SpanVal.setObjectName("CO2SpanVal")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(210, 60, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.co2 = QtWidgets.QLabel(Dialog)
        self.co2.setGeometry(QtCore.QRect(90, 100, 41, 21))
        self.co2.setText("")
        self.co2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.co2.setObjectName("co2")
        self.h2o = QtWidgets.QLabel(Dialog)
        self.h2o.setGeometry(QtCore.QRect(90, 120, 41, 21))
        self.h2o.setText("")
        self.h2o.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.h2o.setObjectName("h2o")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(160, 100, 61, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(160, 120, 61, 21))
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(230, 90, 31, 21))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(330, 90, 21, 21))
        self.label_21.setObjectName("label_21")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(230, 120, 251, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.connectLI6262 = QtWidgets.QPushButton(Dialog)
        self.connectLI6262.setGeometry(QtCore.QRect(410, 10, 75, 23))
        self.connectLI6262.setObjectName("connectLI6262")
        self.CO2Zero = QtWidgets.QPushButton(Dialog)
        self.CO2Zero.setGeometry(QtCore.QRect(360, 60, 121, 23))
        self.CO2Zero.setObjectName("CO2Zero")
        self.CO2Span = QtWidgets.QPushButton(Dialog)
        self.CO2Span.setGeometry(QtCore.QRect(360, 90, 121, 23))
        self.CO2Span.setObjectName("CO2Span")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(330, 170, 21, 21))
        self.label_22.setObjectName("label_22")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(230, 200, 251, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(230, 170, 31, 21))
        self.label_20.setObjectName("label_20")
        self.H2OSpanVal = QtWidgets.QLineEdit(Dialog)
        self.H2OSpanVal.setGeometry(QtCore.QRect(270, 170, 51, 20))
        self.H2OSpanVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.H2OSpanVal.setObjectName("H2OSpanVal")
        self.H2OSpan = QtWidgets.QPushButton(Dialog)
        self.H2OSpan.setGeometry(QtCore.QRect(360, 170, 121, 23))
        self.H2OSpan.setObjectName("H2OSpan")
        self.H2OZero = QtWidgets.QPushButton(Dialog)
        self.H2OZero.setGeometry(QtCore.QRect(360, 140, 121, 23))
        self.H2OZero.setObjectName("H2OZero")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(230, 140, 101, 21))
        self.label_23.setObjectName("label_23")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LI-6262"))
        Dialog.setWindowIcon(QtGui.QIcon('licor-logo.jpg'))
        self.CO2SpanVal.setText(_translate("Dialog", "400"))
        self.label_2.setText(_translate("Dialog", "LI-6262 COM Port:"))
        self.label_5.setText(_translate("Dialog", "CO2:"))
        self.label_6.setText(_translate("Dialog", "H2O:"))
        self.label_15.setText(_translate("Dialog", "μmol/mol"))
        self.label_16.setText(_translate("Dialog", "mmol/mol"))
        self.label_19.setText(_translate("Dialog", "Span:"))
        self.label_21.setText(_translate("Dialog", "ppm"))
        self.label_9.setText(_translate("Dialog", "Status"))
        self.connectLI6262.setText(_translate("Dialog", "Connect"))
        self.CO2Zero.setText(_translate("Dialog", "CO2 Zero"))
        self.CO2Span.setText(_translate("Dialog", "CO2 Span"))
        self.label_22.setText(_translate("Dialog", "°C"))
        self.label_20.setText(_translate("Dialog", "Span:"))
        self.H2OSpanVal.setText(_translate("Dialog", "17"))
        self.H2OSpan.setText(_translate("Dialog", "H2O Span"))
        self.H2OZero.setText(_translate("Dialog", "H2O Zero"))
        self.label_23.setText(_translate("Dialog", "Dewpoint"))
