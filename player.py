from client import Client


class Player:
    def __init__(self, client, number):
        self.number = number
        self.client = client
        self.capturedPieces = []
        self.color = 'l' if number == 1 else 'd'
        if number == 2:
            self.client.receive()

    def wins(self):
        pass

    def capture(self, piece):
        self.capturedPieces.append(piece)
