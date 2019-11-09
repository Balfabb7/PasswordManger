import sys
from PyQt5.QtWidgets import QApplication, QWidget

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(500,500)
    win.move(300,300)
    win.setWindowTitle("test")
    win.show()
    sys.exit(app.exec_())

window()