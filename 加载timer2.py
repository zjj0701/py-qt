import sys

from PyQt6 import uic
from PyQt6.QtCore import QDateTime, pyqtSlot, QTimer
from PyQt6.QtWidgets import QLabel, QApplication, QPushButton, QWidget


def show(label: QLabel):
    time = QDateTime.currentDateTime()
    ts = time.toString("yyyy-MM-dd HH:mm:ss")
    label.setText(ts)


@pyqtSlot()
def start(timer, label):
    if not timer.isActive():
        print("on")
        label.show()
        timer.timeout.connect(lambda: show(label))

    timer.start(1000)


@pyqtSlot()
def stop(timer, label: QLabel):
    print("off")
    timer.stop()
    label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui/Qtimer.ui")

    timer = QTimer(ui)
    widget: QWidget = QWidget(ui)
    widget.setWindowTitle("你的时间显示器")
    push1: QPushButton = ui.pushButton
    push2: QPushButton = ui.pushButton_2
    text: QLabel = ui.label
    push1.clicked.connect(lambda: start(timer, text))
    push2.clicked.connect(lambda: stop(timer, text))
    ui.show()
    app.exec()
