'''
File: animal.py
Description: Base animal classes and all the behaviour of the animals.
Author: Amy Lukan
ID: 110458803
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import date


class Animal(ABC):
    # Base class for all animals in the zoo.
    def __init__(self, name, species, age, dietary_needs, category, environment_type):
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
        self.category = category
        self.environment_type = environment_type
        self.health_issues = []

# each subclass must have its own sound
    @abstractmethod
    def make_sound(self):
        pass

# simple animal behaviour
    def eat(self, food):
      if food.lower() in self.dietary_needs:
        return self.name + " the " + self.species + " eats " + food + " happily "
      else:
        return self.name + " refuses to eat " + food + " . "

    def sleep(self, hours=8):
      return self.name + " sleeps for " + str(hours) + " hours."

# add a new health issue for animal
    def report_health_issues(self, description):
      self.health_issues.append({
        "description": description,
        "date": date.today(),
        "status": "open"
        })

# resolve health issue (marked)
    def resolve_health_issues(self):
      for issue in self.health_issues:
         issue["status"] = "resolved"

# return true if the health issue is still opened (used to block movement)
    def is_under_treatment(self):
        for issue in self.health_issues:
            if issue["status"] == "open":
                return True
        return False

    def __str__(self):
     return self.name + " (" + self.species + ", " + self.category + ") - Age: " + str(self.age)

# each animal has a different sound (override absract method)
class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs, environment_type):
        Animal.__init__(self, name, species, age, dietary_needs, "mammal", environment_type)

    def make_sound(self):
        return self.name + " makes a mammal sound."


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, environment_type):
        Animal.__init__(self, name, species, age, dietary_needs, "reptile", environment_type)

    def make_sound(self):
        return self.name + " hisses."


class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs, environment_type):
        Animal.__init__(self, name, species, age, dietary_needs, "bird", environment_type)

    def make_sound(self):
        return self.name + " chirps."
