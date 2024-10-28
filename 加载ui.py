from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/label.ui")

    mylabel:QLabel = ui.label
    print(f"label 是：{mylabel.text()}")
    ui.show()


    sys.exit(app.exec())