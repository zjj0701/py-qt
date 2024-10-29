import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/radiobutton.ui")

    a:QPushButton = ui.radioButton
    print(a.isChecked())
    b: QPushButton = ui.radioButton_2
    print(b.isChecked())
    ui.show()
    app.exec()