import socket
import random

from protocol import send_object, receive_object

HOST = "127.0.0.1"
PORT = 5000


def run_client(client_id):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect((HOST, PORT))

    send_object(sock, client_id)

    status = receive_object(sock)

    print(f"CLIENT {client_id}: {status}")

    if status == "REFUSED":
        sock.close()
        return

    requests = [
        "Cat",
        "Dog",
        "Parrot",
        "UnknownClass"
    ]

    for req in requests:

        send_object(sock, req)

        response = receive_object(sock)

        try:

            if not isinstance(response, list):
                raise TypeError(
                    "Expected list, got "
                    + type(response).__name__
                )

            list(
                map(
                    lambda x:
                    print(
                        f"CLIENT {client_id}: {x}"
                    ),
                    response
                )
            )

        except TypeError as e:
            print(
                f"CLIENT {client_id}: CAST ERROR -> {e}"
            )

    send_object(sock, "END")

    sock.close()


if __name__ == "__main__":

    run_client(random.randint(1, 1000))