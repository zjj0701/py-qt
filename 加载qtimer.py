import sys

from PyQt6 import uic
from PyQt6.QtCore import QTimer, QDateTime, pyqtSlot, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QLabel, QMainWindow


class Mythread(QThread):
    finished = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            pass
class MyWindow():
    def __init__(self):

        self.ui = uic.loadUi("./ui/Qtimer.ui")
        self.timer = QTimer(self.ui)
        self.push1:QPushButton = self.ui.pushButton
        self.push2:QPushButton = self.ui.pushButton_2
        self.text:QLabel = self.ui.label

        self.thread = Mythread()
        self.thread.finished.connect(self.thread_finished)

        self.push1.clicked.connect(lambda: start(self.timer, self.text))
        self.push2.clicked.connect(lambda: stop(self.timer, self.text))

    def start_thread(self):
        self.thread.start()  # 启动线程

    def thread_finished(self):
        self.label.setText("Thread finished!")


def show(label:QLabel):
    time = QDateTime.currentDateTime()
    ts = time.toString("yyyy-MM-dd HH:mm:ss")
    label.setText(ts)

@pyqtSlot()
def start(timer,label):
    if not  timer.isActive():
        print("on")
        label.show()
        timer.timeout.connect(lambda: show(label))

    timer.start(1000)


@pyqtSlot()
def stop(timer,label:QLabel):
    print("off")
    timer.stop()
    label.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.ui.show()
    window.start_thread()
    app.exec()

