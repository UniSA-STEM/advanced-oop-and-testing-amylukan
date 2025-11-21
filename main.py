'''
File: main.py
Description: A brief description of this Python module.
Author: Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''

def main():
    print("Welcome to Simone's Zoo!")

if __name__ == '__main__':
    main()

from animal import Mammal, Bird, Reptile
from enclosure import Enclosure

def main():
    print("=== Zoo Setup ===")
    max = Mammal("Max", "Koala", 2, ["eucalyptus"], "temperate")
    oscar = Bird("Oscar", "Emu", 4, ["pellets"], "grassland")
    lewis = Reptile("Lewis", "Blue-tongued Lizard", 3, ["insects"], "terrarium")

    grove = Enclosure("Koala Grove", 800, "temperate")
    field = Enclosure("Emu Field", 1200, "grassland")
    den = Enclosure("Lizard Den", 200, "terrarium")

    grove.add_animal(max)
    field.add_animal(oscar)
    den.add_animal(lewis)
