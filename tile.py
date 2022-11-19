from PyQt5.QtWidgets import QWidget

from color import RGB
from piece import Piece
from tileHighlight import HighlightManager
import util


class Tile(QWidget):
    def __init__(self, parent, letter, number, length):
        super().__init__(parent)

        self.length = length
        self.x = ord(letter) - ord('a')
        self.y = int(number) - 1

        self.piece = None
        self.color = (self.x % 2 + self.y % 2) % 2
        self.color = RGB(
            255, 255, 255) if not self.color else RGB(80, 120, 60)
        # self.color = '#ffffff' if not self.color else '#466e32'

        self.setGeometry(self.x*length, self.y*length, length, length)
        self.setStyleSheet(f"background-color: {util.rgb2hex(self.color)}")
        self.setAcceptDrops(True)

        self.letter = letter
        self.number = number
        self.code = letter + number

        self.show()

    def setPiece(self, piece):
        self.piece = Piece(self, piece.color, piece.piece)

    def deletePiece(self):
        self.piece = Piece(self, None, None)

    def getPossibleMoves(self):
        return util.possibleMoves[self.piece.code](self.x, self.y, self.piece)

    def displayPossibleMoves(self):
        moves = self.getPossibleMoves()

        for x, y in moves:
            tile = self.parent().tiles[x][y]

    def highlight(self):
        pass

# https://www.pythonguis.com/faq/pyqt-drag-drop-widgets/
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        piece = e.source()
        prevTile = piece.parent()
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
