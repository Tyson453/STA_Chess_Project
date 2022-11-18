def checkTile(tiles, x, y, pieceColor, occupied=True, empty=True):
    if not(0 <= x < 8) and not(0 <= y < 8):
        return False

    tile = tiles[x][y]

    if not tile.piece.code and empty:
        return True
    if tile.piece.code and tile.piece.color != pieceColor and occupied:
        return True
    return False

def getBlackPawnMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    if checkTile(tiles, x, y+1, color, occupied=False):
        possibleMoves.append((x, y+1))

    if checkTile(tiles, x, y+2, color, occupied=False):
        if y == 1:
            possibleMoves.append((x, y+2))

    if checkTile(tiles, x+1, y+1, color, occupied=True, empty=False):
        possibleMoves.append((x+1, y+1))

    if checkTile(tiles, x-1, y+1, color, occupied=True, empty=False):
        possibleMoves.append((x-1, y+1))

    return possibleMoves

def getWhitePawnMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    if checkTile(tiles, x, y-1, color, occupied=False):
        possibleMoves.append((x, y-1))

    if checkTile(tiles, x, y-2, color, occupied=False):
        if y == 6:
            possibleMoves.append((x, y-2))

    if checkTile(tiles, x+1, y-1, color, occupied=True, empty=False):
        possibleMoves.append((x+1, y-1))

    if checkTile(tiles, x-1, y-1, color, occupied=True, empty=False):
        possibleMoves.append((x-1, y-1))

def getBlackBishopMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        for i in range(1,9):
            dx *= i
            dy *= i

            nx, ny = x+dx, y+dy

            if not(0 <= nx < 8) or not(0 <= ny < 8):
                print(nx, ny)
                print()
                break

            print(f"({nx}, {ny}) = {checkTile(tiles, nx, ny, color)}")
            if checkTile(tiles, nx, ny, color):
                possibleMoves.append((nx, ny))

            if tiles[nx][ny].piece.code:
                print(f"Failed at ({nx}, {ny})")
                print()
                break

            print()

    return possibleMoves

def getWhiteBishopMoves(x, y, piece):
    pass


def getBlackRookMoves(x, y, piece):
    pass

def getWhiteRookMoves(x, y, piece):
    pass

def getBlackKnightMoves(x, y, piece):
    pass

def getWhiteKnightMoves(x, y, piece):
    pass

def getBlackKingMoves(x, y, piece):
    pass

def getWhiteKingMoves(x, y, piece):
    pass

def getBlackQueenMoves(x, y, piece):
    pass

def getWhiteQueenMoves(x, y, piece):
    pass

startingPieces = {
    'a1': 'rd',
    'b1': 'nd',
    'c1': 'bd',
    'd1': 'qd',
    'e1': 'kd',
    'f1': 'bd',
    'g1': 'nd',
    'h1': 'rd',
    
    'a2': 'pd',
    'b2': 'pd',
    'c2': 'pd',
    'd2': 'pd',
    'e2': 'pd',
    'f2': 'pd',
    'g2': 'pd',
    'h2': 'pd',

    
    'a8': 'rl',
    'b8': 'nl',
    'c8': 'bl',
    'd8': 'ql',
    'e8': 'kl',
    'f8': 'bl',
    'g8': 'nl',
    'h8': 'rl',
    
    'a7': 'pl',
    'b7': 'pl',
    'c7': 'pl',
    'd7': 'pl',
    'e7': 'pl',
    'f7': 'pl',
    'g7': 'pl',
    'h7': 'pl',
}

possibleMoves = {
    'pd': getBlackPawnMoves,
    'bd': getBlackBishopMoves,
    'rd': getBlackRookMoves,
    'nd': getBlackKnightMoves,
    'kd': getBlackKingMoves,
    'qd': getBlackQueenMoves,
    'pl': getWhitePawnMoves,
    'bl': getWhiteBishopMoves,
    'rl': getWhiteRookMoves,
    'nl': getWhiteKnightMoves,
    'kl': getWhiteKingMoves,
    'ql': getWhiteQueenMoves,
}

def getDisplacement(tile1, tile2):
    return (tile1.x - tile2.x, tile1.y - tile2.y)

def getSlope(dx, dy):
    pass