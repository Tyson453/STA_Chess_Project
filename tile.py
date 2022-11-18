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

        self.color = (self.x%2 + self.y%2) % 2
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
        del self.piece

        self.piece = Piece(self, piece.pixmap.imagePath, piece.length)

        del piece

    def deletePiece(self):
        self.piece = Piece(self, None, self.piece.length)

    def getPossibleMoves(self):
        return util.possibleMoves.get(self.piece, None)

# https://www.pythonguis.com/faq/pyqt-drag-drop-widgets/
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        piece = e.source()
        prevTile = piece.parent

        slope = util.getSlope(*util.getDisplacement(self, prevTile))
        if slope not in self.getPossibleMoves():
            e.ignore()

        if self.piece.color == piece.color:
            e.ignore()

        
            
        self.setPiece(piece)
        e.accept()