from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TextLine(QLineEdit):
    def __init__(self, parent=None):
        super(TextLine, self).__init__(parent)
        self.setEchoMode(QLineEdit.Password)


class Label(QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        self.setStyleSheet('color: limegreen; '
                            'font-size: 26px; '
                            'font-family: Comic Sans MS, Comic Sans, cursive')


class Label1(QPushButton):
    def __init__(self, parent=None):
        super(Label1, self).__init__(parent)
        self.setMouseTracking(True)
        self.textbox = UiPasswordWindow()
        self.setStyleSheet('color: limegreen; '
                           'background-color: black;'
                           'font-size: 16px;'
                           'font-family: Comic Sans MS, Comic Sans, cursive;')

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet('color: red; '
                               'background-color: black;'
                               'font-size: 16px;'
                               'font-family: Comic Sans MS, Comic Sans, cursive;')

    def leaveEvent(self, event):
        self.setStyleSheet('color: limegreen; '
                           'background-color: black;'
                           'font-size: 16px;'
                           'font-family: Comic Sans MS, Comic Sans, cursive;')


class UiPasswordWindow(QWidget):
    def setupUI(self, passwordWindow):
        self.setMouseTracking(True)
        passwordWindow.setObjectName("Password Entry Window")
        passwordWindow.resize(500, 300)
        self.setAutoFillBackground(True)
        color = self.palette()
        color.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(color)
        self.label = Label(self)
        self.label.setText("Password: ")
        self.label.adjustSize()
        self.label2 = Label(self)
        self.label2.setText("Username: ")
        self.label2.adjustSize()
        self.label3 = Label1(self)
        self.label3.setText("Show Password")
        self.label3.adjustSize()
        self.label3.clicked.connect(self.clicked)
        self.label4 = Label1(self)
        self.label4.setText("Hide Password")
        self.label4.adjustSize()
        self.label4.clicked.connect(self.clicked2)
        self.textbox = TextLine(self)
        self.textbox2 = QLineEdit(self)
        self.submit = QPushButton("Login", self)
        self.hbox1 = QHBoxLayout(self)
        self.hbox1.addStretch(1)
        self.hbox1.addWidget(self.label.setGeometry(100, 60, 150, 100))
        self.hbox1.addWidget(self.textbox.setGeometry(230, 97, 150, 30))
        self.hbox1.addWidget(self.label2.setGeometry(100, 20, 150, 100))
        self.hbox1.addWidget(self.textbox2.setGeometry(230, 57, 150, 30))
        self.hbox1.addWidget(self.label3.setGeometry(250, 130, 110, 20))
        self.hbox1.addWidget(self.label4.setGeometry(250, 150, 110, 20))
        self.vbox1 = QVBoxLayout(self)
        self.vbox1.addStretch(1)
        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addWidget(self.submit.setStyleSheet('background-color: limegreen; border-radius: 4px; font-size: 20px'))
        self.vbox1.addWidget(self.submit.setGeometry(100, 140, 80, 30))
        self.vbox1.setGeometry(QRect(0, 0, 500, 180))
        self.setLayout(self.vbox1)

    def clicked(self):
        self.textbox.setEchoMode(QLineEdit.Normal)

    def clicked2(self):
        self.textbox.setEchoMode(QLineEdit.Password)

