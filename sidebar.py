from PyQt5.QtWidgets import QWidget, QLabel, QFrame
from PyQt5.QtCore import Qt

from moveTable import MoveTable


class Sidebar(QWidget):
    def __init__(self, parent, w, h, x):
        print(parent)
        super().__init__(parent)

        self.x = x
        self.y = 0
        self.w = w
        self.h = h

        self.setGeometry(self.x, self.y, self.w, self.h)

        print(self.parent())
        self.createPlayerLabel()
        self.createMoveTable()

    def update(self):
        self.playerLabel.setText(
            f"Player {self.parent().currentPlayer.number}")

    def createPlayerLabel(self):
        self.playerLabel = QLabel(self)
        self.playerLabel.setGeometry(10, 10, self.w - 20, self.h - 450)
        self.playerLabel.setAlignment(Qt.AlignCenter)
        self.playerLabel.setStyleSheet(
            "font-size: 36pt; border: 4px solid black;")
        self.playerLabel.setText(
            f"Player {self.parent().currentPlayer.number}")

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
