from PyQt5 import QtWidgets, QtGui, QtCore

from client import Client
from game import Game
from server import Server


class Window(QtWidgets.QMainWindow):
    def __init__(self, w, h, x, y):
        super().__init__()
        self.activeScreens = []

        self.setWindowTitle('Chess')
        self.setGeometry(x, y, w, h)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("background-color: #777777")

        # Create and show the menu screen
        self.initMenuScreen()
        self.menuScreen.show()

        self.show()

    def initMenuScreen(self):
        self.menuScreen = QtWidgets.QWidget(self)
        self.activeScreens.append(self.menuScreen)

        self.menuScreen.setAttribute(QtCore.Qt.WA_StyleSheet)
        self.menuScreen.setGeometry(0, 0, self.width(), self.height())

        # Variables for the "Create Game" and "Join Game" buttons
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

        # Create the "Create Game" button
        self.createGameButton: QtWidgets.QPushButton = QtWidgets.QPushButton(
            "Create Game", self.menuScreen)
        self.createGameButton.setGeometry(
            self.width()//2 - bw//2, self.height()//5, bw, bh)
        self.createGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.createGameButton.setStyleSheet(bStyleSheet)
        self.createGameButton.setFont(bFont)

        # Run self.initCreateGameScreen when self.createGameButton is clicked
        self.createGameButton.clicked.connect(self.initCreateGameScreen)

        # Create the "Join Game" button
        self.joinGameButton = QtWidgets.QPushButton(
            "Join Game", self.menuScreen)
        self.joinGameButton.setGeometry(
            self.width()//2 - bw//2, self.height()*3//5, bw, bh)
        self.joinGameButton.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.joinGameButton.setStyleSheet(bStyleSheet)
        self.joinGameButton.setFont(bFont)

        # Run self.initJoinGameScreen when self.joinGameButton is clicked
        self.joinGameButton.clicked.connect(self.initJoinGameScreen)

    def initCreateGameScreen(self):
        self.createGameScreen = QtWidgets.QWidget(self)
        self.activeScreens.append(self.createGameScreen)

        self.createGameScreen.setGeometry(0, 0, self.width(), self.height())

        labelFont = QtGui.QFont("serif", 36, -1, False)
        lw, lh = 600, 100

        # Label that will display the Join code
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
        self.activeScreens.append(self.joinGameScreen)

        self.joinGameScreen.setGeometry(0, 0, self.width(), self.height())

        font = QtGui.QFont("serif", 34, -1, False)
        w, h = self.width()*3//8, self.height()//4

        # Text entry for entering the Join code
        self.codeEntry = QtWidgets.QLineEdit(self.joinGameScreen)
        self.codeEntry.setGeometry(
            self.width()//2, self.height()//2 - h//2, w, h)
        self.codeEntry.setFont(font)
        self.codeEntry.setStyleSheet(
            "border-color: #666666;border-width: 4px;")

        # When the user presses enter, call self.createClient
        # self.codeEntry.returnPressed.connect(self.createClient)
        self.codeEntry.returnPressed.connect(self.joinGame)

        self.codeEntryLabel = QtWidgets.QLabel(
            "Game code: ", self.joinGameScreen)
        self.codeEntryLabel.setGeometry(
            self.width()//4 - self.width()//8, self.height()//2 - h//2, w, h)
        self.codeEntryLabel.setFont(font)

        self.joinGameScreen.show()

    def createGame(self):
        # Change screens
        self.menuScreen.hide()
        self.createGameScreen.show()

        # Start server
        self.gameServer = Server(self)
        self.gameServer.start()
        self.game = Game(self, self.width(), self.height(), 0, 0)

        # Connect server playerNumberReachedSignal to onPlayerNumberReached Slot
        self.gameServer.playerNumberReachedSignal.connect(self.onPlayerNumberReached)

        # Get and display the join code
        code = self.gameServer.code
        self.codeLabel.setText("Game Code: " + code)

        # Create client for player 1
        self.createClient(code=code, num=1)

    def joinGame(self):
        self.createClient(num=2)

        # Change screens
        self.menuScreen.hide()
        self.joinGameScreen.show()

        self.game = Game(self, self.width(), self.height(), 0, 0)
        for screen in self.activeScreens:
            screen.hide()

        self.game.start(self.client, True)
        # Client will be created when the join code is entered into self.codeEntry

    def createClient(self, code=None, num=2):
        self.num = num
        # Get the code if one is not provided
        if not code:
            code = self.codeEntry.displayText()

        # Create client and player
        self.client = Client(code)
        # self.player = Player(num, self.client)

    @QtCore.pyqtSlot(bool)
    def onPlayerNumberReached(self, value):
        if value:
            self.game.start(self.gameServer.players[self.num-1], self.num)
            for screen in self.activeScreens:
                screen.hide()
        else:
            self.game.stop()
