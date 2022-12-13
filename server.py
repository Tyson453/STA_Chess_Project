from PyQt5 import QtCore

import socket
import string
import threading

from game import Game
from logger import Logger
import Constants
from player import Player

digs = string.digits + string.ascii_letters


class Server(QtCore.QObject):
    playerNumberReachedSignal = QtCore.pyqtSignal(bool)

    def __init__(self, window):
        super().__init__()
        self.window = window

        # Constants
        self.SERVER = Constants.SERVER
        self.PORT = Constants.DEFAULT_PORT
        self.ADDR = Constants.ADDR
        self.DISCONNECT_MSG = Constants.DISCONNECT_MSG
        self.HEADER = Constants.HEADER
        self.FORMAT = Constants.FORMAT

        self.logger = Logger()
        self.maxConnections = 1
        self.players = []

        # Encode the address which will be used for the join code
        self.code = self.encodeAddress(self.ADDR)

        # Create the server and bind it to the address
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handleClient(self, conn, addr):
        self.log(f"New connection: {addr[0]}:{addr[1]}")

        connected = True
        while connected:
            # Receive the header from the client
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            # If msg_length is empty, skip the next steps
            if not msg_length:
                continue

            # Receive the message from the client
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(self.FORMAT)

            # Disconnect if the client sends the disconnect message
            if msg == self.DISCONNECT_MSG:
                connected = False
                break

            # Log the message and send the response
            self.logger.log(f"{addr[0]}:{addr[1]}", f'"{msg}"')
            conn.send("!RECEIVED".encode(self.FORMAT))

        # If the client disconnects, close the connection
        conn.close()
        self.log(f"{addr[0]} disconnected")
        self.playerNumberReachedSignal.emit(False)

    def start(self):
        self.log("Starting...")
        self.server.listen()
        self.log(f"Listening on {self.SERVER}:{self.PORT}")

        # Create a new thread that handles any incoming connections
        self.thread = threading.Thread(
            target=self.handleConnections, daemon=True)
        self.thread.start()

    def handleConnections(self):
        # While the server is running and max connections hasn't been reached
        while True and threading.active_count() - 2 < self.maxConnections:
            # Accept the incoming client
            conn, addr = self.server.accept()
            self.players.append(Player(len(self.players)+1, conn, addr))
            # Create a thread that will handle the messages between the server and new client
            thread = threading.Thread(
                target=self.handleClient, args=(conn, addr), daemon=True)
            thread.start()

        self.log(f"Max connections ({self.maxConnections}) reached")
        self.playerNumberReachedSignal.emit(True)

    def encodeAddress(self, addr):
        # Convert ip address to decimal
        ip = sum([(int(num)*(256**i))
                 for i, num in enumerate(addr[0].split('.')[::-1])])
        port = addr[1]

        # Add port if port is not the default port (5050)
        code = int(str(ip) + (str(port) if port !=
                   Constants.DEFAULT_PORT else ''))

        # Convert code into base 36 to reduce the code to 6 digits
        digits = []
        while code:
            digits.append(digs[code % Constants.JOIN_CODE_BASE])
            code //= Constants.JOIN_CODE_BASE

        code = ''.join(digits[::-1])

        return f"{code:0>7s}".upper()

    def log(self, msg):
        self.logger.log(self, msg)

    def __repr__(self):
        return "SERVER"


# if __name__ == '__main__':
#     logger = Logger()
#     server = socket.gethostbyname(socket.gethostname())
#     port = 5050
#     addr = (server, port)
#     discon_msg = "!DISCONNECT"
#     header = 64
#     _format = 'utf-8'

#     s = Server('')
#     s.start()
