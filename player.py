class Player:
    def __init__(self, number, client):
        self.number = number
        self.client = client
        self.capturedPieces = []

    def wins(self):
        pass

    def capture(self, piece):
        self.capturedPieces.append(piece)
