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

    def start(self, player):
        self.player = player

        self.turn = 0

        self.sidebar = Sidebar(
            self, self.width()-self.height(), self.height(), self.height())
        self.board = Board(self, self.width(), self.height(
        ), self.height()//8, flipped=(True if self.player.number == 2 else False))

        self.show()

    def checkGameState(self):
        if any([p.piece == 'k' for p in self.player.capturedPieces]):
            self.player.wins()

    def registerMove(self, start, end, move, received=False):
        self.sidebar.moveTable.addMove(move)

        if not received:
            msg = f"!MOVE({start}, {end}, {move})"

            self.player.client.send(msg)

            self.nextTurn()

    def nextTurn(self):
        self.turn += 1
        self.turn %= 2

        self.sidebar.update()

    def stop(self):
        del self

    @QtCore.pyqtSlot(str)
    def messageSlot(self, value):
        prefix, args = self.decodeMessage(value)

        if prefix == "!MOVE":
            self.registerMove(*args, received=True)
