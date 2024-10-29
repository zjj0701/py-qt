from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QTextEdit
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/textedit.ui")

    myedit:QTextEdit = ui.textEdit
    myedit2:QTextEdit = ui.textEdit_2
    myedit.setTextColor(QtGui.QColor(255, 0, 0))
    myedit.setPlainText("hello")

    myedit2.setHtml("<a href='www.baidu.com'>baidu</a>")

    ui.show()


    sys.exit(app.exec())