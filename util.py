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
    'p': [],
    'b': [],
    'r': [],
    'n': [],
    'k': [],
    'q': [],
}

def getDisplacement(tile1, tile2):
    return (tile1.x - tile2.x, tile1.y - tile2.y)

def getSlope(dx, dy):
    pass