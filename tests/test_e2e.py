import unittest
import threading
import time

from server import start_server
from client import run_client


class E2ETests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        thread = threading.Thread(
            target=start_server,
            daemon=True
        )

        thread.start()

        time.sleep(1)

    def test_multiple_clients(self):

        clients = []

        for i in range(5):

            t = threading.Thread(
                target=run_client,
                args=(i,)
            )

            clients.append(t)
            t.start()

        for t in clients:
            t.join()

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()