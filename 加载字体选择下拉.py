import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QComboBox

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui = uic.loadUi('./ui/fontcombox.ui')

    ui.show()
    app.exec()
    print("end...")
