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
    @abstractmethod
    def make_sound(self):
        pass


class Mammal(Animal):
    pass


class Reptile(Animal):
    pass


class Bird(Animal):
    pass
