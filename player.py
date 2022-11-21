class Player:
    def __init__(self, game, name, number, color):
        self.game = game
        self.name = name
        self.number = number
        self.color = color
        self.capturedPieces = []

    def wins(self):
        pass

    def capture(self, piece):
        self.capturedPieces.append(piece)

        self.game.checkGameState()