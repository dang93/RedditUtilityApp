# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RedditCommentsDesign.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditSearchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchInput.setGeometry(QtCore.QRect(20, 10, 221, 23))
        self.lineEditSearchInput.setObjectName("lineEditSearchInput")
        self.radioButtonSubmission = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonSubmission.setGeometry(QtCore.QRect(110, 40, 91, 17))
        self.radioButtonSubmission.setObjectName("radioButtonSubmission")
        self.radioButtonUser = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonUser.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.radioButtonUser.setChecked(True)
        self.radioButtonUser.setObjectName("radioButtonUser")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.tableViewComments = QtWidgets.QTableView(self.centralwidget)
        self.tableViewComments.setGeometry(QtCore.QRect(20, 70, 761, 521))
        self.tableViewComments.setObjectName("tableViewComments")
        self.lineEditFilterKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFilterKey.setGeometry(QtCore.QRect(510, 10, 271, 23))
        self.lineEditFilterKey.setObjectName("lineEditFilterKey")
        self.labelFilterBy = QtWidgets.QLabel(self.centralwidget)
        self.labelFilterBy.setGeometry(QtCore.QRect(430, 10, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelFilterBy.setFont(font)
        self.labelFilterBy.setObjectName("labelFilterBy")
        self.comboBoxFilterOptions = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxFilterOptions.setGeometry(QtCore.QRect(430, 40, 81, 23))
        self.comboBoxFilterOptions.setObjectName("comboBoxFilterOptions")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButtonSubmission.setText(_translate("MainWindow", "Submission"))
        self.radioButtonUser.setText(_translate("MainWindow", "User"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.labelFilterBy.setText(_translate("MainWindow", "Filter By:"))

