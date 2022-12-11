import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "!DISCONNECT"
HEADER = 64
FORMAT = "utf-8"
