#PyQt5 packages
from PyQt5 import QtWidgets, QtCore, QtGui

# Design Files
import RedditCommentsDesign

# Project Files
import RedditAPI
import UtilityFunctions

class RedditWindow(QtWidgets.QMainWindow, RedditCommentsDesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RedditWindow, self).__init__(parent)
        self.setupUi(self)
        self.redditAPI = RedditAPI.RedditAPI()

        self.setFixedSize(self.size())

        self.setupWidgets()
        self.setupConnections()

    def setupWidgets(self):
        # filter combo box
        self.comboBoxItemList = ['subreddit', 'comment']
        self.comboBoxFilterOptions.clear()
        self.comboBoxFilterOptions.addItems(self.comboBoxItemList)

        # table model
        self.tableModel = QtGui.QStandardItemModel(0, 4)
        self.tableModel.setHorizontalHeaderLabels(
            ['subreddit', 'comment', 'score', 'date'])

        # filter proxy model
        self.filterProxyModel = QtCore.QSortFilterProxyModel()
        self.filterProxyModel.setSourceModel(self.tableModel)
        self.filterProxyModel.setFilterKeyColumn(0)

        self.tableViewComments.setModel(self.filterProxyModel)

        # table view
        self.tableViewComments.setColumnWidth(0, 151)
        self.tableViewComments.setColumnWidth(1, 435)
        self.tableViewComments.setColumnWidth(2, 45)
        self.tableViewComments.setColumnWidth(3, 100)
        self.tableViewComments.setFixedSize(self.tableViewComments.size())
        self.tableViewComments.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed)
        self.tableViewComments.setSortingEnabled(True)
        self.tableViewComments.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableViewComments.horizontalScrollBar().setEnabled(False)

    def setupConnections(self):
        # combo box
        self.comboBoxFilterOptions.currentIndexChanged.connect(
            self.changeFilterKey)

        # filter line edit
        self.lineEditFilterKey.textChanged.connect(
            self.filterProxyModel.setFilterRegExp)

        # search button
        self.pushButtonSearch.clicked.connect(self.searchClicked)

        # search line edit
        self.lineEditSearchInput.returnPressed.connect(
            self.pushButtonSearch.click)

    def searchClicked(self):
        input = self.lineEditSearchInput.text()
        if input == '':
            return

        if self.radioButtonUser.isChecked():
            if self.redditAPI.userExists(input) is False:
                msg = 'Username \'' + input + '\' does not exit'
                UtilityFunctions.showQMessageBox(msg)
                return
            else:
                self.result = self.redditAPI.getUserComments(input)

        elif self.radioButtonSubmission.isChecked():
            if self.redditAPI.submissionExists(input) is False:
                msg = 'Submission URL: \'' + input + '\' does not exists'
                UtilityFunctions.showQMessageBox(msg)
                return
            else:
                self.result = self.redditAPI.getSubmissionTopLevelComments(
                    input)
        self.fillTable()

    def fillTable(self):
        for row, comment in enumerate(self.result):
            commentData = comment.getMinimalInfo()
            self.tableModel.setItem(row, 0, QtGui.QStandardItem(
                commentData['subreddit']))
            self.tableModel.setItem(row, 1, QtGui.QStandardItem(
                commentData['commentText']))
            self.tableModel.setItem(row, 2, QtGui.QStandardItem(
                commentData['score']))
            self.tableModel.setItem(row, 3, QtGui.QStandardItem(
                commentData['date']))

        self.tableViewComments.setModel(self.filterProxyModel)

    def changeFilterKey(self):
        value = self.comboBoxFilterOptions.currentText()
        self.lineEditFilterKey.clear()
        if value == 'subreddit':
            self.filterProxyModel.setFilterKeyColumn(0)
        elif value == 'comment':
            self.filterProxyModel.setFilterKeyColumn(1)