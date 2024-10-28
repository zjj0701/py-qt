from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("test")
win.resize(400,300)
win.move(500,500)
win.show()

label = QLabel()
label.setText("hello")
label.setParent(win)
label.move(80,80)
label.resize(50,50)
label.show()
label.setStyleSheet("background-color: green")

sys.exit(app.exec())

