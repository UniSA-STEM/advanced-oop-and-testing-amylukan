'''
File: enclosure.py
Description: A brief description of this Python module.
Author:  Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Enclosure:
    """Houses animals of one species and one environment."""
    def __init__(self, name, size_m2, environment_type):
        if size_m2 <= 0:
            raise ValueError('Size must be greater than zero.')
        self.name = name
        self.size_m2 = size_m2
        self.environment_type = environment_type.lower()
        self.cleanliness = 80
        self.animals = []
        self.species_restriction = None

