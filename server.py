import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(2)

clients = []
clients_lock = threading.Lock()

print("Chess Server Started...")
print("Waiting for players...")


def send_message(client, message):
    try:
        client.sendall((message + "\n").encode())
        return True
    except Exception as e:
        print("Send Error:", e)
        return False


def remove_client(client):
    with clients_lock:
        if client in clients:
            clients.remove(client)

    try:
        client.close()
    except:
        pass

    print("Player disconnected")


def broadcast(sender, message):
    disconnected = []

    with clients_lock:
        current_clients = clients.copy()

    for client in current_clients:
        if client != sender:
            if not send_message(client, message):
                disconnected.append(client)

    for client in disconnected:
        remove_client(client)


def handle_client(client, address):

    buffer = ""

    try:
        while True:

            data = client.recv(2048)

            if not data:
                break

            buffer += data.decode()

            while "\n" in buffer:

                message, buffer = buffer.split("\n", 1)

                message = message.strip()

                if not message:
                    continue

                print(
                    "Received from client:",
                    message
                )

                broadcast(
                    client,
                    message
                )

    except Exception as e:

        print(
            "Client Error:",
            e
        )

    finally:

        remove_client(client)


while True:

    client, address = server.accept()

    with clients_lock:

        if len(clients) >= 2:

            print(
                "Game already has 2 players..."
            )

            send_message(
                client,
                "FULL"
            )

            try:
                client.close()
            except:
                pass

            continue

        clients.append(client)

        player_number = len(clients)

    print(
        "Connected:",
        address
    )

    # =========================================
    # PLAYER ASSIGNMENT
    # =========================================

    if player_number == 1:

        send_message(
            client,
            "WHITE"
        )

        print(
            "Assigned WHITE"
        )

    elif player_number == 2:

        send_message(
            client,
            "BLACK"
        )

        print(
            "Assigned BLACK"
        )

        print(
            "Both players connected!"
        )

        print(
            "Game Started!"
        )

    thread = threading.Thread(
        target=handle_client,
        args=(client, address),
        daemon=True
    )

    thread.start()