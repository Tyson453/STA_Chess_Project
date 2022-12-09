import socket

from logger import Logger

class Client:
    def __init__(self, logger: Logger, addr: tuple, discon_msg: str, header: int, _format: str):
        self.ADDR = addr
        self.DISCONNECT_MSG = discon_msg
        self.HEADER = header
        self.FORMAT = _format

        self.logger = logger

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        msg = msg.encode(self.FORMAT)
        msg_length = len(msg)

        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(msg)

        self.log(f"Message \"{msg}\" sent")

    def log(self, msg):
        self.logger.log(self, msg)

    def __repr__(self):
        return f"{self.ADDR[0]}:{self.ADDR[1]}"

if __name__ == '__main__':
    logger = Logger()
    server = socket.gethostbyname(socket.gethostname())
    port = 5050
    addr = (server, port)
    discon_msg = "!DISCONNECT"
    header = 64
    _format = 'utf-8'

    c = Client(logger, addr, discon_msg, header, _format)