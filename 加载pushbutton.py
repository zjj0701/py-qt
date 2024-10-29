import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('./ui/pushbutton.ui')
    button:QPushButton = ui.pushButton
    button2:QPushButton = ui.pushButton_2
    print(button.text())
    print(button2.text())
    ui.show()

    app.exec()