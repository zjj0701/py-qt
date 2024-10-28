from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/linelabel.ui")

    lineedit:QLineEdit = ui.lineEdit
    lineedit2:QLineEdit = ui.lineEdit_2
    # lineedit2.setFocus()
    print(f"label 是：{lineedit.text()}")
    lineedit.clear()
    ui.show()


    sys.exit(app.exec())