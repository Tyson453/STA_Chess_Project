from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData

from piece import Piece
import util


class Tile(QWidget):
    def __init__(self, parent, letter, number, length):
        self.piece = None

        self.x = ord(letter) - ord('a')
        self.y = int(number) - 1

        self.color = (self.x % 2 + self.y % 2) % 2
        self.color = '#ffffff' if not self.color else '#74b56c'

        super().__init__(parent)
        self.setGeometry(self.x*length, self.y*length, length, length)
        self.setStyleSheet(f"background-color: {self.color}")

        self.letter = letter
        self.number = number

        self.code = letter + number

        self.setAcceptDrops(True)

        self.show()

    def setPiece(self, piece):
        self.piece = Piece(self, piece.color, piece.piece, piece.length)

    def deletePiece(self):
        self.piece = Piece(self, None, None, self.piece.length)

    def getPossibleMoves(self):
        return util.possibleMoves[self.piece.code](self.x, self.y, self.piece)

# https://www.pythonguis.com/faq/pyqt-drag-drop-widgets/
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        piece = e.source()
        prevTile = piece.parent
        displacement = (self.x, self.y)

        possibleMoves = prevTile.getPossibleMoves()
        if displacement not in possibleMoves:
            e.ignore()
            return

        if self.piece.color == piece.color:
            e.ignore()
            return

        self.setPiece(piece)
        e.accept()
