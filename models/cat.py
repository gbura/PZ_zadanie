from dataclasses import dataclass

@dataclass
class Cat:
    name: str
    age: int

    def __str__(self):
        return f"Cat(name={self.name}, age={self.age})"