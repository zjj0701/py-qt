import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton


def cal(a: int, b: int, line3: QLineEdit) -> int:
    line3.setText(str(a + b))

def style(line3:QLineEdit):
    line3.setStyleSheet("background-color: rgb(255, 255, 255);")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/caohanshu.ui")

    line: QLineEdit = ui.lineEdit
    line2: QLineEdit = ui.lineEdit_2

    pushbutton: QPushButton = ui.pushButton

    line3: QLineEdit = ui.lineEdit_3
    line3.setHidden(True)
    pushbutton.clicked.connect(lambda: cal(int(line.text()), int(line2.text()), line3))
    pushbutton.clicked.connect(lambda: style(line3))
    ui.show()
    app.exec()
