# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonGetStarted = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetStarted.setGeometry(QtCore.QRect(350, 270, 100, 23))
        self.pushButtonGetStarted.setObjectName("pushButtonGetStarted")
        self.labelWelcome = QtWidgets.QLabel(self.centralwidget)
        self.labelWelcome.setGeometry(QtCore.QRect(20, 200, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelWelcome.setFont(font)
        self.labelWelcome.setObjectName("labelWelcome")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonGetStarted.setText(_translate("MainWindow", "Get Started!"))
        self.labelWelcome.setText(_translate("MainWindow", "Welcome to my Reddit comment utility app!"))

