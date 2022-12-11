import socket

SERVER = socket.gethostbyname(socket.gethostname())
DEFAULT_PORT = 5050
ADDR = (SERVER, DEFAULT_PORT)
DISCONNECT_MSG = "!DISCONNECT"
HEADER = 64
FORMAT = "utf-8"
