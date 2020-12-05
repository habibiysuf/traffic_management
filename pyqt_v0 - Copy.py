from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "SMART TRAFFIC MANAGEMENT CONTROL"
        self.top = 100
        self.left = 300
        self.width = 800
        self.height = 600
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

Ap = QApplication(sys.argv)
window = Window()
sys.exit(Ap.exec())
