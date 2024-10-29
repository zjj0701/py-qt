import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QComboBox

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui = uic.loadUi('./ui/combox.ui')
    combox:QComboBox = ui.comboBox
    combox.addItem("sb")
    combox.addItems(["sb1","sb2"])
    print(combox.currentText(),combox.currentIndex())
    ui.show()
    app.exec()
    print("end...")
    combox.clear()