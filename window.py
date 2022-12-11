from PyQt5 import QtWidgets, QtGui, QtCore


from client import Client
from player import Player
from server import Server


class Window(QtWidgets.QMainWindow):
    def __init__(self, w, h, x, y):
        super().__init__()

        self.setWindowTitle('Chess')
        self.setGeometry(x, y, w, h)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("background-color: #777777")

        self.initMenuScreen()

        self.menuScreen.show()

        self.show()

    def initMenuScreen(self):
        self.menuScreen = QtWidgets.QWidget(self)

        self.menuScreen.setAttribute(QtCore.Qt.WA_StyleSheet)
        self.menuScreen.setGeometry(0, 0, self.width(), self.height())

        bw, bh = self.width()//2 + 50, self.height()//5
        bFont = QtGui.QFont("serif", 48, -1, False)
        bStyleSheet = """
            QPushButton::hover {
                background-color: #bbbbbb;
            }
            QPushButton::!hover {
                background-color: #999999;
            }
        """

        self.createGameButton: QtWidgets.QPushButton = QtWidgets.QPushButton(
            "Create Game", self.menuScreen)
        self.createGameButton.setGeometry(
            self.width()//2 - bw//2, self.height()//5, bw, bh)
        self.createGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.createGameButton.setStyleSheet(bStyleSheet)
        self.createGameButton.setFont(bFont)

        self.createGameButton.clicked.connect(self.initCreateGameScreen)

        self.joinGameButton = QtWidgets.QPushButton(
            "Join Game", self.menuScreen)
        self.joinGameButton.setGeometry(
            self.width()//2 - bw//2, self.height()*3//5, bw, bh)
        self.joinGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.joinGameButton.setStyleSheet(bStyleSheet)
        self.joinGameButton.setFont(bFont)

        self.joinGameButton.clicked.connect(self.initJoinGameScreen)

        self.menuScreen.hide()

    def initCreateGameScreen(self):
        self.createGameScreen = QtWidgets.QWidget(self)

        self.createGameScreen.setGeometry(0, 0, self.width(), self.height())
        # self.createGameScreen.setAttribute(QtCore.Qt.WA_StyledBackground)

        labelFont = QtGui.QFont("serif", 36, -1, False)
        lw, lh = 500, 100

        self.codeLabel = QtWidgets.QLabel("Test", self.createGameScreen)
        self.codeLabel.setGeometry(
            self.width()//2 - lw//2, self.height()//2 - lh//2, lw, lh)
        self.codeLabel.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.codeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.codeLabel.setFont(labelFont)
        self.codeLabel.show()

        self.createGame()

    def initJoinGameScreen(self):
        self.client = None

        self.joinGameScreen = QtWidgets.QWidget(self)

        self.joinGameScreen.setGeometry(0, 0, self.width(), self.height())

        font = QtGui.QFont("serif", 34, -1, False)
        w, h = self.width()*3//8, self.height()//4

        self.codeEntry = QtWidgets.QLineEdit(self.joinGameScreen)
        self.codeEntry.setGeometry(
            self.width()//2, self.height()//2 - h//2, w, h)
        self.codeEntry.setFont(font)
        # self.codeEntry.setAlignment(QtCore.Qt.AlignLeft)
        # self.codeEntry.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.codeEntry.setStyleSheet(
            "border-color: #666666;border-width: 4px;")
        self.codeEntry.returnPressed.connect(self.createClient)

        self.codeEntryLabel = QtWidgets.QLabel(
            "Game code: ", self.joinGameScreen)
        self.codeEntryLabel.setGeometry(
            self.width()//4 - self.width()//8, self.height()//2 - h//2, w, h)
        self.codeEntryLabel.setFont(font)
        # self.codeEntryLabel.setAlignment(QtCore.Qt.AlignRight)

        self.joinGame()

    def createGame(self):
        self.menuScreen.hide()
        self.createGameScreen.show()

        # Start server
        self.gameServer = Server()
        self.gameServer.start()

        code = self.gameServer.code
        self.codeLabel.setText("Game Code: " + code)

        self.createClient(code=code, num=1)

    def joinGame(self):
        self.menuScreen.hide()
        self.joinGameScreen.show()

    def createClient(self, code=None, num=2):
        if not code:
            code = self.codeEntry.displayText()

        self.client = Client(code)
        self.player = Player(num, self.client)
