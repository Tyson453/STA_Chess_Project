from PyQt5 import QtWidgets
from piece import Piece
from tile import Tile

import util


class Board(QtWidgets.QWidget):
    def __init__(self, parent, w, h, tileLength):
        super().__init__(parent)
        self.setGeometry(0, 0, w, h)

        self.tiles = []

        for char in 'abcdefgh':
            row = []
            for num in '12345678':
                tile = Tile(self, char, num, tileLength)
                piece, color = self.getStartingPiece(char, num)
                tile.setPiece(Piece(tile, color, piece))
                # row.append(tile)
            self.tiles.append(row)

        self.show()

    def getStartingPiece(self, char, num):
        piece = util.startingPieces.get(char+num, None)
        if piece:
            return piece[0], piece[1]
        return (None, None)

    def unhighlightAll(self):
        for row in self.tiles:
            for tile in row:
                tile.unhighlight()
