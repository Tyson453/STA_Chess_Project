import socket
import string
import threading

from logger import Logger
import Constants

digs = string.digits + string.ascii_letters


class Server:
    def __init__(self):
        self.SERVER = Constants.SERVER
        self.PORT = Constants.DEFAULT_PORT
        self.ADDR = Constants.ADDR
        self.DISCONNECT_MSG = Constants.DISCONNECT_MSG
        self.HEADER = Constants.HEADER
        self.FORMAT = Constants.FORMAT

        self.code = self.encodeAddress(self.ADDR)

        self.logger = Logger()
        self.maxConnections = 2

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handleClient(self, conn, addr):
        self.log(f"New connection: {addr[0]}:{addr[1]}")

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if not msg_length:
                continue

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(self.FORMAT)

            if msg == self.DISCONNECT_MSG:
                connected = False
                break

            self.logger.log(f"{addr[0]}:{addr[1]}", f'"{msg}"')
            conn.send("!RECEIVED".encode(self.FORMAT))

        conn.close()
        self.log(f"{addr[0]} disconnected")

    def start(self):
        self.log("Starting...")
        self.server.listen()
        self.log(f"Listening on {self.SERVER}:{self.PORT}")

        self.thread = threading.Thread(
            target=self.handleConnections)
        self.thread.start()

    def handleConnections(self):
        while True and threading.active_count() - 2 < self.maxConnections:
            conn, addr = self.server.accept()
            thread = threading.Thread(
                target=self.handleClient, args=(conn, addr))
            thread.start()
        self.log(f"Max connections ({self.maxConnections}) reached")

    def encodeAddress(self, addr):
        # Convert ip address to decimal
        ip = sum([(int(num)*(256**i))
                 for i, num in enumerate(addr[0].split('.')[::-1])])
        port = addr[1]

        # Add port if port is not the default port (5050)
        code = int(str(ip) + (str(port) if port !=
                   Constants.DEFAULT_PORT else ''))

        # Convert code into base 32 to reduce the code to 6 digits
        digits = []
        while code:
            digits.append(digs[code % 32])
            code //= 32

        code = ''.join(digits[::-1])

        return f"{code:06s}".upper()

    def log(self, msg):
        self.logger.log(self, msg)

    def __repr__(self):
        return "SERVER"


if __name__ == '__main__':
    logger = Logger()
    server = socket.gethostbyname(socket.gethostname())
    port = 5050
    addr = (server, port)
    discon_msg = "!DISCONNECT"
    header = 64
    _format = 'utf-8'

    s = Server('')
    s.start()
