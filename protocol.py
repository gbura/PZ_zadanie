import pickle
import struct


def send_object(sock, obj):
    data = pickle.dumps(obj)

    sock.sendall(struct.pack("!I", len(data)))
    sock.sendall(data)


def receive_object(sock):
    raw_len = recv_all(sock, 4)

    if not raw_len:
        return None

    length = struct.unpack("!I", raw_len)[0]

    data = recv_all(sock, length)

    return pickle.loads(data)


def recv_all(sock, length):
    data = b''

    while len(data) < length:
        packet = sock.recv(length - len(data))

        if not packet:
            return None

        data += packet

    return data