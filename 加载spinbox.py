import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QSpinBox

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/qspinbox.ui")
    spinbox:QSpinBox = ui.spinBox
    spinbox.setPrefix(":")
    print(spinbox.text())

    ui.show()
    app.exec()