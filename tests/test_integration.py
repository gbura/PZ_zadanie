import unittest
import pickle

from models.cat import Cat


class IntegrationTests(unittest.TestCase):

    def test_serialization(self):

        cat = Cat("Milo", 2)

        data = pickle.dumps(cat)

        restored = pickle.loads(data)

        self.assertEqual(cat, restored)


if __name__ == "__main__":
    unittest.main()