'''
File: enclosure.py
Description: Deals with housing the animals, in what enclosure and enforcing enclosure rules.
Author:  Amy Lukan
ID: 110458803
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Enclosure:
    # Houses animals of one species and one environment.
    def __init__(self, name, size_m2, environment_type):
        if size_m2 <= 0:
            raise ValueError('Size must be greater than zero.')
        self.name = name
        self.size_m2 = size_m2
        self.environment_type = environment_type.lower()
        self.cleanliness = 80
        self.animals = []
        self.species_restriction = None

# adds an animal if the rules are met
    def add_animal(self, animal):
        if self.environment_type.lower() != self.environment_type:
            raise ValueError('Encountered an unexpected environment type.')
        if self.species_restriction is not None and animal.species != self.species_restriction:
            raise ValueError('Only one species per enclosure.')
        if animal.is_under_treatment():
            raise ValueError('Cannot move an animal under treatment.')
        self.animals.append(animal)
        if self.species_restriction is None:
            self.species_restriction = animal.species

# removes an animal (unless under treatment)
    def remove_animal(self, animal):
       if animal.is_under_treatment():
        raise ValueError('Cannot remove an animal under treatment.')
       self.animals.remove(animal)

# basic enclosure requirements
    def feed_all(self, food):
      results = []
      for a in self.animals:
        results.append(a.eat(food))
      return results

    def clean(self):
      self.cleanliness = 100
      return self.name + " cleaned to " + str(self.cleanliness) + "%. "

    def status_report(self):
      report = "Enclosure: " + self.name + " (" + self.environment_type + ")\n"
      if len(self.animals) == 0:
          report += "  No animals currently.\n"
      else:
        for a in self.animals:
            report += "  - " + a.name + " (" + a.species + ")\n"
      return report