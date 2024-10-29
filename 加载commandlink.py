import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QCommandLinkButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/commandlink.ui")

    co:QCommandLinkButton = ui.commandLinkButton
    print(f"command is:{co.text()}")
    print(f"描述是：{co.description()}")
    ui.show()
    app.exec()