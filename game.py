from ctypes import wstring_at
import sys

from PyQt5.QtWidgets import QMainWindow
from board import Board
from player import Player


class Game(QMainWindow):
    def __init__(self, w, h, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.setWindowTitle('Chess')
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.board = Board(self, self.w, self.h, self.h//8)

        self.player1 = Player(self, 'Tyson', 1, 'l')
        self.player2 = Player(self, 'Whelan', 2, 'd')
        self.players = [self.player1, self.player2]
        self.currentPlayer = self.player1

        self.show()

    def getPlayers(self):
        pass

    def play(self):
        turn = -1

        while not self.gameIsOver():
            turn += 1

            self.currentPlayer = self.players[turn]

            self.currentPlayer.move()
