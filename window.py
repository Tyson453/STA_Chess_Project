from PyQt5 import QtWidgets, QtGui, QtCore

import random

class Window(QtWidgets.QMainWindow):
    def __init__(self, w, h, x, y):
        super().__init__()

        self.setWindowTitle('Chess')
        self.setGeometry(x, y, w, h)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("background-color: #777777")

        self.initMenuScreen()
        self.initCreateGameScreen()
        self.initJoinGameScreen()

        # self.menuScreen.show()
        self.createGameScreen.show()

        self.show()

    def initMenuScreen(self):
        self.menuScreen = QtWidgets.QWidget(self)

        self.menuScreen.setAttribute(QtCore.Qt.WA_StyleSheet)
        self.menuScreen.setGeometry(0, 0, self.width(), self.height())

        bw, bh = self.width()//2, self.height()//5
        bFont = QtGui.QFont("serif", 48, -1, False)
        bStyleSheet = """
            QPushButton::hover {
                background-color: #bbbbbb;
            }
            QPushButton::!hover {
                background-color: #999999;
            }
        """

        self.createGameButton = QtWidgets.QPushButton("Create Game", self.menuScreen)
        self.createGameButton.setGeometry(self.width()//4, self.height()//5, bw, bh)
        self.createGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.createGameButton.setStyleSheet(bStyleSheet)
        self.createGameButton.setFont(bFont)

        self.createGameButton.clicked.connect(self.createGame)
        
        self.joinGameButton = QtWidgets.QPushButton("Join Game", self.menuScreen)
        self.joinGameButton.setGeometry(self.width()//4, self.height()*3//5, bw, bh)
        self.joinGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.joinGameButton.setStyleSheet(bStyleSheet)
        self.joinGameButton.setFont(bFont)

        self.joinGameButton.clicked.connect(self.joinGame)

        lw, lh = 300, 100

        # self.codeLabel = QtWidgets.QLabel("Test", self.menuScreen)
        # self.codeLabel.setGeometry(self.width()//2 - lw//2, self.height()//2 - lh//2, lw, lh)
        # self.codeLabel.setAttribute(QtCore.Qt.WA_StyledBackground)
        # self.codeLabel.setStyleSheet("background-color: white")
        # self.codeLabel.show()

        self.menuScreen.hide()

    def initCreateGameScreen(self):
        self.createGameScreen = QtWidgets.QWidget(self)

        lw, lh = 300, 100

        self.codeLabel = QtWidgets.QLabel("Test", self.createGameScreen)
        self.codeLabel.setGeometry(self.width()//2 - lw//2, self.height()//2 - lh//2, lw, lh)
        self.codeLabel.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.codeLabel.setStyleSheet("background-color: white")
        self.codeLabel.show()

        self.createGameScreen.hide()

    def initJoinGameScreen(self):
        self.joinGameScreen = QtWidgets.QWidget(self)

        self.joinGameScreen.hide()

    def createGame(self):
        self.menuScreen.hide()
        self.createGameScreen.show()
        code = self.generateCode()
        self.codeLabel.setText("Game Code: " + code)
        self.codeLabel.show()
        print(self.codeLabel.pos())

    def joinGame(self):
        self.menuScreen.hide()
        self.joinGameScreen.show()
        print("Joining Game")

    def generateCode(self):
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"

        code = random.choices(chars, k=6)

        return ''.join(code)