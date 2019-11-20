from PasswordManger.Main import MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())