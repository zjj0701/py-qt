import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QListWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./ui/listwidget.ui')
    listwidget: QListWidget = ui.listWidget
    lis = ["a", "b", "c"]
    listwidget.addItems(lis)
    listwidget.setWindowTitle("test")
    ui.show()
    app.exec()
