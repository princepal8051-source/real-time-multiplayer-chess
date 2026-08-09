import socket

class Network:

    def __init__(self):

        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.host = "127.0.0.1"
        self.port = 5555

        self.addr = (
            self.host,
            self.port
        )

        self.connect()

    def connect(self):

        try:

            self.client.connect(
                self.addr
            )

        except:

            pass

    def send(self, data):

        try:

            self.client.send(
                str(data).encode()
            )

        except:

            pass

    def receive(self):

        try:

            return self.client.recv(
                2048
            ).decode()

        except:

            return None