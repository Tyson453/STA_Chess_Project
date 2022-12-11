import math
import socket

from logger import Logger
import Constants


class Client:
    def __init__(self, code):
        # Constants
        self.ADDR = self.decodeAddress(code)
        self.SERVER, self.PORT = self.ADDR
        self.DISCONNECT_MSG = Constants.DISCONNECT_MSG
        self.HEADER = Constants.HEADER
        self.FORMAT = Constants.FORMAT

        # Conect to the server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        # self.send(self.DISCONNECT_MSG)

    def send(self, msg):
        # Encode the message
        msg = msg.encode(self.FORMAT)

        # Create the header message
        send_length = str(len(msg)).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        # Send the header message (tells the server how large the actual message will be so it doesn't lose information)
        self.client.send(send_length)
        # Send the actual message
        self.client.send(msg)

        # Get the response from the server
        response = self.client.recv(2048).decode(self.FORMAT)

    def decodeAddress(self, code):
        # Check if the code includes the port
        withPort = len(code) > 6
        # Decode from base 32 to decimal
        code = int(code, 32)

        # Get the port and ip address
        if withPort:
            port = code[-4:]
            ip = code[:-4]
        else:
            port = Constants.DEFAULT_PORT
            ip = code

        # Turn the decimal IP address into IPv4
        octets = []

        for i in range(4):
            x = ip/256
            y = math.floor(x) * 256
            octets.append(str(ip - y))
            ip = math.floor(x)

        ip = '.'.join(octets[::-1])

        return (ip, port)

    def __repr__(self):
        return f"{self.ADDR[0]}"
        # return f"{self.ADDR[0]}:{self.ADDR[1]}"


if __name__ == '__main__':
    c = Client()
