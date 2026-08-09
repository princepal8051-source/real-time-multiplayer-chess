import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))


def receive():

    while True:

        try:

            message = client.recv(1024)

            print(
                "\nReceived:",
                message.decode()
            )

        except:

            break


threading.Thread(
    target=receive,
    daemon=True
).start()

while True:

    msg = input("Send: ")

    client.send(
        msg.encode()
    )