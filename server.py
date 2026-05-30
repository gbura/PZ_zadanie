import socket
import threading
import random
import time

from repository import Repository
from protocol import send_object, receive_object

HOST = "127.0.0.1"
PORT = 5000

MAX_CLIENTS = 3

repository = Repository()

active_clients = 0
lock = threading.Lock()


def handle_client(conn, addr):

    global active_clients

    try:

        client_id = receive_object(conn)

        with lock:

            if active_clients >= MAX_CLIENTS:
                print(f"REFUSED client {client_id}")

                send_object(conn, "REFUSED")
                return

            active_clients += 1

        print(f"CONNECTED client {client_id}")

        send_object(conn, "OK")

        while True:

            request = receive_object(conn)

            if request is None:
                break

            if request == "END":
                break

            time.sleep(random.uniform(0.5, 2.0))

            objects = repository.get_objects_by_type(request)

            if objects:
                send_object(conn, objects)

                print(
                    f"Sent {objects} to client {client_id}"
                )

            else:
                send_object(conn, repository.data["dog_1"])

                print(
                    f"Sent wrong object to client {client_id}"
                )

    finally:

        with lock:
            active_clients = max(0, active_clients - 1)

        conn.close()


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))
    server.listen()

    print("SERVER STARTED")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":
    start_server()