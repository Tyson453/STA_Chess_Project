from PyQt5 import QtWidgets
from board import Board
from player import Player
from sidebar import Sidebar


class Game(QtWidgets.QWidget):
    def __init__(self, parent, w, h, x, y, server):
        super().__init__(parent)

        self.setWindowTitle('Chess')
        self.setGeometry(x, y, w, h)

        self.server = server

        self.players = self.server.players
        self.currentPlayer = self.players[0]

        self.turn = 0

        self.sidebar = Sidebar(self, self.width()-self.height(), self.height(), self.height())

        self.show()

    def checkGameState(self):
        for player in self.players:
            if any([p.piece == 'k' for p in player.capturedPieces]):
                player.wins()

    def registerMove(self, move):
        self.sidebar.moveTable.addMove(move)

    def nextTurn(self):
        self.turn += 1
        self.turn %= 2

        self.currentPlayer = self.players[self.turn]

        self.sidebar.update()
