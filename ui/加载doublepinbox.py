import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDoubleSpinBox

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/Qdoublepinbpx.ui")
    d:QDoubleSpinBox = ui.doubleSpinBox


    ui.show()
    app.exec()
