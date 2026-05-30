from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    breed: str

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"