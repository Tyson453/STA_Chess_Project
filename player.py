class Player:
    def __init__(self, number, connection):
        self.number = number
        self.client = connection
        self.capturedPieces = []

    def wins(self):
        pass

    def capture(self, piece):
        self.capturedPieces.append(piece)
