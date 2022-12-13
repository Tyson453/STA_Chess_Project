from PyQt5 import QtWidgets, QtCore
from board import Board
from player import Player
from sidebar import Sidebar


class Game(QtWidgets.QWidget):
    def __init__(self, parent, w, h, x, y):
        super().__init__(parent)

        self.setWindowTitle('Chess')
        self.setGeometry(x, y, w, h)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        # self.setStyleSheet("background-color: black")

        self.hide()

    def start(self, player, number):
        self.player = player

        self.turn = 0

        self.sidebar = Sidebar(self, self.width()-self.height(), self.height(), self.height())
        self.board = Board(self, self.width(), self.height(), self.height()//8, flipped=(True if number == 2 else False))

        self.show()

    def checkGameState(self):
        if any([p.piece == 'k' for p in self.player.capturedPieces]):
            self.player.wins()

    def registerMove(self, move):
        self.sidebar.moveTable.addMove(move)

        msg = f"p{self.player.number}: {move}"

        # print(self.player.client)
        self.player.client.send(move)

        self.nextTurn()

    def nextTurn(self):
        self.turn += 1
        self.turn %= 2

        self.sidebar.update()

    def stop(self):
        del self
