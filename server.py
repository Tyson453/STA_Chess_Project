import socket
import threading

from logger import Logger

class Server:
    def __init__(self, logger: Logger, addr: tuple, discon_msg: str, header: int, _format: str):
        self.ADDR = addr
        self.DISCONNECT_MSG = discon_msg
        self.HEADER = header
        self.FORMAT = _format

        self.logger = logger

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        self.log("Starting...")
        self.start()

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
            
            self.log(f"Message \"{msg}\" received from {addr[0]}:{addr[1]}")
            conn.send("Message received".encode(self.FORMAT))

        conn.close()

    def start(self):
        server.listen()
        self.log(f"Listening on {self.SERVER}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=self.handleClient, args=(conn, addr))
            thread.start()
            self.log(f"Active Connections: {threading.activeCount() - 1}")

    def log(self, msg):
        self.logger.log(self, msg)

    def __repr__(self):
        return "SERVER"
