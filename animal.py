'''
File: animal.py
Description: A brief description of this Python module.
Author: Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    """Base class for all animals in the zoo."""
    def __init__(self, name: str, species: str, age: int, dietary_needs: list):
        if not name or not species:
            raise ValueError("Name and species cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not dietary_needs:
            raise ValueError("Dietary needs cannot be empty.")
        self.name = name
        self.species = species
        self.age = age
        self.dietary_needs = [d.lower() for d in dietary_needs]
        self.health_issues = []

    @abstractmethod
    def make_sound(self):
        pass


class Mammal(Animal):
    pass


class Reptile(Animal):
    pass


class Bird(Animal):
    pass
