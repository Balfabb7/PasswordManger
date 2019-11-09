from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UiPasswordWindow(QWidget):
    def setupUI(self, passwordWindow):
        passwordWindow.setObjectName("Password Entry Window")
        passwordWindow.resize(300, 500)
        self.setAutoFillBackground(True)
        color = self.palette()
        color.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(color)
        self.label = QLabel("New Page", self)
        self.label.setStyleSheet('color: limegreen; '
                                 'font-size: 26px; '
                                 'font-family: Comic Sans MS, Comic Sans, cursive')
        self.label.adjustSize()
        self.label.move(100, 200)



