class MoveChecker:
    def __init__(self):
        pass

    def checkTile(tiles, x, y, pieceColor, occupied=True, empty=True):
        if not(0 <= x < 8) and not(0 <= y < 8):
            return False

        tile = tiles[x][y]

        if not tile.piece.code and empty:
            return True
        if tile.piece.code and tile.piece.color != pieceColor and occupied:
            return True
        return False

