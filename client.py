import socket


class Client:
    # TODO: Make these constant somewhere else
    HEADER = 64
    FORMAT = "utf-8"
    DISCONNECT_MSG = "!DISCONNECT"

    def __init__(self):
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.ADDR = (self.SERVER, self.PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        self.send("Hello world!")

    def send(self, msg):
        msg = msg.encode(self.FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(msg)
        self.client.recv(2048)

    def __repr__(self):
        return f"[{self.SERVER}:{self.client.listen}]"


if __name__ == '__main__':
    c = Client()

    c.send(Client.DISCONNECT_MSG)
