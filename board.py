from PyQt5 import QtWidgets
from piece import Piece
from tile import Tile

import util


class Board(QtWidgets.QWidget):
    def __init__(self, parent, w, h, tileLength, flipped=False):
        super().__init__(parent)
        self.setGeometry(0, 0, w, h)

        self.flipped = flipped
        self.tiles = []

        letters = 'abcdefgh'
        numbers = '12345678'
        if self.flipped:
            letters = letters[::-1]
            numbers = numbers[::-1]

        for i, char in enumerate(letters):
            row = []
            for j, num in enumerate(numbers):
                tile = Tile(self, char, num, i, j, tileLength)
                piece, color = self.getStartingPiece(char, num)
                tile.setPiece(Piece(tile, color, piece))
                row.append(tile)
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

    def getTile(self, code):
        x = ord(code[0]) - ord('a')
        y = int(code[1])-1

        if self.flipped:
            x = abs(x-7)
            y = abs(y-7)

        tile = self.tiles[x][y]
        return tile
