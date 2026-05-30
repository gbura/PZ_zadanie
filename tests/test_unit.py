import unittest

from models.cat import Cat
from repository import Repository


class UnitTests(unittest.TestCase):

    def test_equals(self):

        a = Cat("Milo", 2)
        b = Cat("Milo", 2)

        self.assertEqual(a, b)

    def test_repository(self):

        repo = Repository()

        cats = repo.get_objects_by_type("Cat")

        self.assertEqual(len(cats), 4)


if __name__ == "__main__":
    unittest.main()