import sys

from PyQt5 import QtWidgets, QtGui

print("Starting Cam Sound...")

class Label(QtWidgets.QLabel):
    def __init__(self, Parent, Txt):
        super().__init__()
        self.setParent(Parent)
        self.setText(Txt)

class Button(QtWidgets.QPushButton):
    def __init__(self, Parent, Txt, W:int=None, H:int=None, Icon:QtGui.QIcon=None):
        super().__init__()
        self.setParent(Parent)
        self.setText(Txt)
        self.setStyleSheet("background:#fff; color: #000; padding:5px")

        if W != None and H != None:
            self.setMinimumSize(W,H)

        if Icon:
            self.setIcon(Icon)
        self.show()

class Player(QtWidgets.QGridLayout):
    def __init__(self, Parent):
        super().__init__()
        self.setParent(Parent)
        self.playBtn = Button(self, "Play")
        self.StopBtn = Button(self, "Stop")

    

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cam Sound - No track")
        self.setMinimumSize(800,600)
        self.setStyleSheet("background:#000011; margin:10px; color:#fff")
        self.player = Player(self)
        self.show()

app = QtWidgets.QApplication(sys.argv)

UI = App()

sys.exit(app.exec())