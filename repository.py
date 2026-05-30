from models.cat import Cat
from models.dog import Dog
from models.parrot import Parrot


class Repository:

    def __init__(self):
        self.data = {}

        self.data["cat_1"] = Cat("Milo", 2)
        self.data["cat_2"] = Cat("Luna", 3)
        self.data["cat_3"] = Cat("Simba", 5)
        self.data["cat_4"] = Cat("Nala", 1)

        self.data["dog_1"] = Dog("Rex", "Labrador")
        self.data["dog_2"] = Dog("Max", "Beagle")
        self.data["dog_3"] = Dog("Rocky", "Bulldog")
        self.data["dog_4"] = Dog("Lucky", "Husky")

        self.data["parrot_1"] = Parrot("Kiwi", 30)
        self.data["parrot_2"] = Parrot("Rio", 50)
        self.data["parrot_3"] = Parrot("Coco", 15)
        self.data["parrot_4"] = Parrot("Pablo", 25)

    def get_objects_by_type(self, class_name):
        result = []

        for value in self.data.values():
            if value.__class__.__name__.lower() == class_name.lower():
                result.append(value)

        return result