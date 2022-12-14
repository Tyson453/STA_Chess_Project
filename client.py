import math
import socket

from logger import Logger
import Constants


class Client:
    DISCONNECT_MSG = Constants.DISCONNECT_MSG
    HEADER = Constants.HEADER
    FORMAT = Constants.FORMAT

    def __init__(self, code: str = None, client: socket.socket = None, addr: tuple = None):
        if code:
            self.ADDR = self.decodeAddress(code)
            self.SERVER, self.PORT = self.ADDR

            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)

        elif client and addr:
            self.ADDR = addr
            self.SERVER, self.PORT = self.ADDR

            self.client = client

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
        response = self.client.recv(2048)

    def decodeAddress(self, code):
        # Check if the code includes the port
        withPort = len(code) > 7
        # Decode from base 36 to decimal
        code = int(code, Constants.JOIN_CODE_BASE)

        # Get the port and ip address
        if withPort:
            port = int(str(code)[-4:])
            ip = int(str(code)[:-4])
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
