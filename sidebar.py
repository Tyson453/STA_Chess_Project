from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

from moveTable import MoveTable


class Sidebar(QtWidgets.QWidget):
    def __init__(self, parent, w, h, x):
        super().__init__(parent)

        self.x = x
        self.y = 0
        self.w = w
        self.h = h

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("background-color: white")

        self.createPlayerLabel()
        self.createMoveTable()

        self.show()

    def update(self):
        self.playerLabel.setText(
            f"Player {self.parent().turn+1}")

    def createPlayerLabel(self):
        self.playerLabel = QtWidgets.QLabel(self)
        self.playerLabel.setGeometry(10, 10, self.w - 20, self.h//5)
        self.playerLabel.setAlignment(Qt.AlignCenter)
        self.playerLabel.setStyleSheet(
            "font-size: 36pt; border: 4px solid black;")
        self.update()

        self.playerLabel.show()

    def createMoveTable(self):
        self.moveTable = MoveTable(
            self,
            self.playerLabel.x(),
            self.playerLabel.height() + 20,
            self.playerLabel.width(),
            self.h - self.playerLabel.height() - 30
        )

        self.moveTable.show()
