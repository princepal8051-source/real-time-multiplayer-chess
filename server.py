import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen(2)

clients = []

print("Chess Server Started...")
print("Waiting for players...")


def handle_client(client):

    while True:

        try:

            message = client.recv(1024)

            if not message:
                break

            for c in clients:

                if c != client:

                    c.send(message)

        except:

            break

    clients.remove(client)

    client.close()


while True:

    client, address = server.accept()

    clients.append(client)

    print("Connected:", address)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()