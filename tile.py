from PyQt5.QtWidgets import QWidget

from color import RGB
from piece import Piece
import util


class Tile(QWidget):
    def __init__(self, parent, letter, number, length):
        super().__init__(parent)

        self.length = length
        self.x = ord(letter) - ord('a')
        self.y = int(number) - 1
        self.pos = (self.x, self.y)

        self.piece = None
        self.color = (self.x % 2 + self.y % 2) % 2
        self.color = RGB(
            255, 255, 255) if not self.color else RGB(150, 190, 100)

        self.setGeometry(self.x*length, self.y*length, length, length)
        self.setStyleSheet(
            f"background-color: {util.rgb2hex(self.color)}"
        )
        self.setAcceptDrops(True)

        self.letter = letter
        self.number = number
        self.code = letter + number

        self.show()

    def setPiece(self, piece):
        self.deletePiece()
        self.piece = Piece(self, piece.color, piece.piece)

    def deletePiece(self):
        if self.piece:
            self.piece.hide()
        del self.piece
        self.piece = Piece(self, None, None)

    def getPossibleMoves(self):
        return util.possibleMoves[self.piece.code](self.x, self.y, self.piece)

    def highlightPossibleMoves(self):
        moves = self.getPossibleMoves()

        for x, y in moves:
            tile = self.parent().tiles[x][y]
            tile.highlight()

    def highlight(self):
        self.piece.showHighlight(self.piece.code)

    def unhighlight(self):
        self.piece.hideHighlight()
        self.setStyleSheet(f"background-color: {util.rgb2hex(self.color)}")

    def getMove(self, piece):
        piecePrefix = '' if piece.piece == 'p' else piece.piece.upper()
        move = self.code
        return piecePrefix + move

    def dragEnterEvent(self, e):
        if e.source().color != self.parent().parent().currentPlayer.color:
            e.ignore()
        else:
            e.accept()

    def dropEvent(self, e):
        player = self.parent().parent().currentPlayer
        pos = e.pos()
        piece = e.source()
        prevTile = piece.parent()
        newPos = (self.x, self.y)

        if prevTile.color != player.color:
            e.ignore()

        possibleMoves = prevTile.getPossibleMoves()
        if newPos not in possibleMoves:
            e.ignore()
            return

        if self.piece.color == piece.color:
            e.ignore()
            return

        capturedPiece = self.setPiece(piece)

        if capturedPiece:
            player.capture(capturedPiece)

        move = self.getMove(piece)
        self.parent().parent().registerMove(move)

        e.accept()
