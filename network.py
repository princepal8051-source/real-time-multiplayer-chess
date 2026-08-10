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

        self.buffer = ""

        self.connect()


    # =========================================
    # CONNECT
    # =========================================

    def connect(self):

        try:

            self.client.connect(
                self.addr
            )

            print(
                "Connected to server"
            )

        except Exception as e:

            print(
                "Connection Error:",
                e
            )


    # =========================================
    # SEND
    # =========================================

    def send(self, data):

        try:

            message = str(data) + "\n"

            self.client.sendall(
                message.encode()
            )

            print(
                "Sent:",
                data
            )

        except Exception as e:

            print(
                "Send Error:",
                e
            )


    # =========================================
    # RECEIVE
    # =========================================

    def receive(self):

        try:

            while "\n" not in self.buffer:

                data = self.client.recv(
                    2048
                )

                if not data:

                    return None

                self.buffer += data.decode()

            message, self.buffer = (
                self.buffer.split(
                    "\n",
                    1
                )
            )

            return message.strip()

        except Exception as e:

            print(
                "Receive Error:",
                e
            )

            return None