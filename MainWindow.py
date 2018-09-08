#PyQt5 packages
from PyQt5 import QtGui, QtWidgets, QtCore

# Design Files
import MainWindowDesign

# Misc packages
import sys

# Project files
import RedditWindow

class MainWindow(QtWidgets.QMainWindow, MainWindowDesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.size())

        self.labelWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWelcome.setText('Welcome to my Reddit comment utility app!')

        self.pushButtonGetStarted.clicked.connect(self.openRedditWindow)

    def openRedditWindow(self):
        self.redditWindow = RedditWindow.RedditWindow()
        self.hide()
        self.redditWindow.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()