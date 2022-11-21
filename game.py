from ctypes import wstring_at
import sys

from PyQt5.QtWidgets import QMainWindow
from board import Board
from player import Player
from sidebar import Sidebar
from highlightManager import HighlightManager

class Game(QMainWindow):
    def __init__(self, w, h, x, y):
        super().__init__()

        self.highlightManager = HighlightManager()

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.setWindowTitle('Chess')
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.player1 = Player(self, 'Tyson', 1, 'l')
        self.player2 = Player(self, 'Whelan', 2, 'd')
        self.players = [self.player1, self.player2]
        self.currentPlayer = self.player1

        self.board = Board(self, self.w, self.h, self.h//8)
        self.sidebar = Sidebar(self, self.w-self.h, self.h, self.h)

        self.turn = 0

        self.show()

    def getPlayers(self):
        pass

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