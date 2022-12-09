import socket
import threading

# TODO: Add logging


class Server:
    # Bytes
    HEADER = 64
    MESSAGE_LENGTH = 0
    FORMAT = 'utf-8'
    DISCONNECT_MSG = "!DISCONNECT"

    def __init__(self):
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.ADDR = (self.SERVER, self.PORT)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        # Log server start
        print(f"[SERVER] Starting...")
        self.start()

    def handleClient(self, conn, addr):
        # Log client connected
        print(f"[SERVER] {addr} Connected")

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if not msg_length:
                continue

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(self.FORMAT)
            # msg = conn.recv(self.MESSAGE_LENGTH).decode(self.FORMAT)
            if msg == self.DISCONNECT_MSG:
                connected = False
                # Log disconnection
                print(f"[SERVER] {addr} Disconnected")

            # Log message received
            print(f"[SERVER] Message \"{msg}\" received from {type(addr)}")
            self.send(conn, "Message received")

        conn.close()

    def send(self, conn, msg):
        conn.send(msg.encode(self.FORMAT))

    def start(self):
        self.server.listen()
        # Log f"Listening on {SERVER}"
        print(f"[SERVER] Listening on port {self.SERVER}")

        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(
                target=self.handleClient,
                args=(conn, addr)
            )
            thread.start()
            # Log active connections
            print(
                f"[SERVER] Active Connections: {threading.active_count() - 1}")

    def __repr__(self):
        return "[SERVER]"


if __name__ == '__main__':
    s = Server()
