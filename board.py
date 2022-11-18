from PyQt5.QtWidgets import QWidget

from piece import Piece
from tile import Tile
import util

class Board(QWidget):
    def __init__(self, parent, width, height, tile_length):
        super().__init__(parent)
        self.setGeometry(0, 0, width, height)

        self.tiles = []

        for char in 'abcdefgh':
            row = []
            for num in '12345678':
                tile = Tile(self, char, num, tile_length)
                piece, color = self.getStartingPiece(char, num)
                tile.setPiece(Piece(tile, color, piece, tile_length))
                row.append(tile)
            self.tiles.append(row)

        self.show()

    def getStartingPiece(self, char, num):
        piece = util.startingPieces.get(char+num, None)
        if piece:
            return piece[0], piece[1]
        return (None, None)