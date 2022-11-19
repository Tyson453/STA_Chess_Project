def checkTile(tiles, x, y, pieceColor, occupied=True, empty=True):
    if not (0 <= x < 8 and 0 <= y < 8):
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

    return possibleMoves


def getBishopMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for i in range(1, 9):
            nx, ny = x+dx*i, y+dy*i

            if not (0 <= nx < 8) or not (0 <= ny < 8):
                break

            if checkTile(tiles, nx, ny, color):
                possibleMoves.append((nx, ny))

            if tiles[nx][ny].piece.code:
                break

    return possibleMoves


def getRookMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        for i in range(1, 9):
            nx, ny = x+dx*i, y+dy*i

            if not (0 <= nx < 8) or not (0 <= ny < 8):
                break

            if checkTile(tiles, nx, ny, color):
                possibleMoves.append((nx, ny))

            if tiles[nx][ny].piece.code:
                break

    return possibleMoves


def getKnightMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        nx, ny = x+dx, y+dy

        if checkTile(tiles, nx, ny, color):
            possibleMoves.append((nx, ny))

    return possibleMoves


def getKingMoves(x, y, piece):
    possibleMoves = []
    color = piece.color
    tiles = piece.parent.parent().tiles

    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+dx, y+dy

        if checkTile(tiles, nx, ny, color):
            possibleMoves.append((nx, ny))

    return possibleMoves


def getQueenMoves(x, y, piece):
    return getBishopMoves(x, y, piece) + getRookMoves(x, y, piece)


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
    'bd': getBishopMoves,
    'rd': getRookMoves,
    'nd': getKnightMoves,
    'kd': getKingMoves,
    'qd': getQueenMoves,
    'pl': getWhitePawnMoves,
    'bl': getBishopMoves,
    'rl': getRookMoves,
    'nl': getKnightMoves,
    'kl': getKingMoves,
    'ql': getQueenMoves,
    None: lambda x, y, z: []
}
