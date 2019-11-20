from PasswordManger.LoginMain import UiLoginWindow
from PasswordManger.PasswordUi import UiPasswordWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(200, 200, 500, 300)
        self.startUILogin()

    def startUILogin(self):
        self.Login = LoginWindow(self)
        self.setWindowTitle("Main Login")
        self.setCentralWidget(self.Login)
        self.Login.button2.clicked.connect(self.startUIPass)


    def startUIPass(self):
        self.password = PasswordWindow()
        self.setWindowTitle("Password Manual Entry")
        self.setCentralWidget(self.password)
        self.show()


class LoginWindow(QMainWindow, UiLoginWindow):

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUI(self)
        self.show()


class PasswordWindow(QMainWindow, UiPasswordWindow):
    def __init__(self, parent=None):
        super(PasswordWindow, self).__init__(parent)
        self.setupUI(self)


