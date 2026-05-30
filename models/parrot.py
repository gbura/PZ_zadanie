from dataclasses import dataclass

@dataclass
class Parrot:
    name: str
    vocabulary: int

    def __str__(self):
        return f"Parrot(name={self.name}, vocabulary={self.vocabulary})"