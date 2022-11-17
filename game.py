from ctypes import wstring_at
import sys

from PyQt5.QtWidgets import QMainWindow
from board import Board

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

        self.show()