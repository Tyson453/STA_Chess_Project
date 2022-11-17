from PyQt5.QtWidgets import QWidget

from piece import Piece
from tile import Tile
from util import startingPieces

class Board(QWidget):
    def __init__(self, parent, width, height, tile_length):
        super().__init__(parent)
        self.setGeometry(0, 0, width, height)

        self.tiles = []

        for char in 'abcdefgh':
            for num in '12345678':
                tile = Tile(self, char, num, tile_length)
                piece = self.getStartingPiece(char, num)
                if piece:
                    tile.setPiece(Piece(tile, piece, tile_length))
                else:
                    tile.setPiece(Piece(tile, piece, tile_length))
                self.tiles.append(tile)

        self.show()

    def getStartingPiece(self, char, num):
        piece = startingPieces.get(char+num, None)
        if piece:
            return f"images/Chess_{piece}t60.png"
        return None