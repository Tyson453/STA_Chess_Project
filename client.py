import socket

from logger import Logger
import Constants


class Client:
    def __init__(self):
        self.SERVER = Constants.SERVER
        self.PORT = Constants.PORT
        self.ADDR = Constants.ADDR
        self.DISCONNECT_MSG = Constants.DISCONNECT_MSG
        self.HEADER = Constants.HEADER
        self.FORMAT = Constants.FORMAT

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        self.send('000000')
        input('')

        self.send(self.DISCONNECT_MSG)

    def send(self, msg):
        msg = msg.encode(self.FORMAT)
        msg_length = len(msg)

        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(msg)

        response = self.client.recv(2048).decode(self.FORMAT)

    # def log(self, msg):
    #     self.logger.log(self, msg)

    def __repr__(self):
        return f"{self.ADDR[0]}"
        # return f"{self.ADDR[0]}:{self.ADDR[1]}"


if __name__ == '__main__':
    c = Client()
