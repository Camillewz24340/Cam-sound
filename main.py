import sys

from PyQt5 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cam Sound - No track")
        self.width = 1280
        self.height = 720
        self.show()

app = QtWidgets.QApplication(sys.argv)

UI = App()

sys.exit(app.exec())