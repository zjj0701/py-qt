import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/lcdnumber.ui")

    ui.show()
    app.exec()