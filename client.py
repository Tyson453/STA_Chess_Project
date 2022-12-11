import math
import socket

from logger import Logger
import Constants


class Client:
    def __init__(self, code):
        self.ADDR = self.decodeAddress(code)
        self.SERVER, self.PORT = self.ADDR
        self.DISCONNECT_MSG = Constants.DISCONNECT_MSG
        self.HEADER = Constants.HEADER
        self.FORMAT = Constants.FORMAT

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        # self.send(self.DISCONNECT_MSG)

    def send(self, msg):
        msg = msg.encode(self.FORMAT)
        msg_length = len(msg)

        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(msg)

        response = self.client.recv(2048).decode(self.FORMAT)

    def decodeAddress(self, code):
        withPort = len(code) > 6
        code = int(code, 32)

        if withPort:
            port = code[-4:]
            ip = code[:-4]
        else:
            port = Constants.DEFAULT_PORT
            ip = code

        octets = []

        for i in range(4):
            x = ip/256
            y = math.floor(x) * 256
            octets.append(str(ip - y))
            ip = math.floor(x)

        ip = '.'.join(octets[::-1])

        return (ip, port)

    # def log(self, msg):
    #     self.logger.log(self, msg)

    def __repr__(self):
        return f"{self.ADDR[0]}"
        # return f"{self.ADDR[0]}:{self.ADDR[1]}"


if __name__ == '__main__':
    c = Client()
