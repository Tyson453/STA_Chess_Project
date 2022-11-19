class Player:
    def __init__(self, game, name, number, color):
        self.game = game
        self.name = name
        self.number = number
        self.color = color
        self.capturedPieces = []

    def move(self):
        prevBoard = self.game.board.copy()

        while prevBoard == self.game.board:
            pass
