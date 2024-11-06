import sys

from PyQt6.QtCore import QDateTime, pyqtSlot, QTimer
from PyQt6.QtWidgets import QLabel, QApplication, QWidget

from Qtimer import Ui_Form


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

class Myapp(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()


        self.setupUi(self)

        self.timer = QTimer(self)


        self.pushButton.clicked.connect(lambda: start(self.timer, self.label))
        self.pushButton_2.clicked.connect(lambda: stop(self.timer, self.label))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myapp()
    w.show()
    app.exec()
