import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPlainTextEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/plaintextedit.ui")
    edit:QPlainTextEdit = ui.plainTextEdit
    edit.setPlainText("text")

    ui.show()
    sys.exit(app.exec())