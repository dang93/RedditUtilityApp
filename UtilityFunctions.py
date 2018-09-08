from PyQt5 import QtWidgets

def showQMessageBox(message):
    msg = QtWidgets.QMessageBox(text=message)
    msg.setWindowTitle('Reddit Comment Utility App')
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()