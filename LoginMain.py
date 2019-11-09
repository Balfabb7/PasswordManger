from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class UiLoginWindow(QWidget):

    def setupUI(self, loginWindow):
        loginWindow.setObjectName("Login Window")
        loginWindow.resize(500, 300)
        self.setAutoFillBackground(True)
        color = self.palette()
        color.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(color)
        self.label = QLabel("start page ", self)
        self.label.setStyleSheet('color: limegreen; '
                                 'font-size: 50px; '
                                 'font-family: Comic Sans MS, Comic Sans, cursive')
        self.label.adjustSize()
        self.label.setAlignment(Qt.AlignCenter)
        self.button1 = QPushButton("Facial Recognition", self)
        self.button1.setStyleSheet('background-color: limegreen; '
                                   'border-radius: 4px;'
                                   'width: 200px;'
                                   'font-size: 20px')
        self.button2 = QPushButton("Key Press", self)
        self.button2.setStyleSheet('background-color: limegreen; '
                                   'border-radius: 4px;'
                                   'width: 200px;'
                                   'font-size: 20px')
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        vbox.setGeometry(QRect(0, 0, 500, 180))
        self.setLayout(vbox)



