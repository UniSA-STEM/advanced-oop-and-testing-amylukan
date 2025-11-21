'''
File: main.py
Description: A brief description of this Python module.
Author: Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    print("Welcome to Simone's Zoo!")
    print("=== Zoo Setup ===")

    # Create animals
    max = Mammal("Max", "Koala", 2, ["eucalyptus"], "temperate")
    oscar = Bird("Oscar", "Emu", 4, ["pellets"], "grassland")
    lewis = Reptile("Lewis", "Blue-tongued Lizard", 3, ["insects"], "terrarium")

    grove = Enclosure("Koala Grove", 800, "temperate")
    field = Enclosure("Emu Field", 1200, "grassland")
    den = Enclosure("Lizard Den", 200, "terrarium")

    grove.add_animal(max)
    field.add_animal(oscar)
    den.add_animal(lewis)

    print("=== Zoo Operations ===")

    ana = Zookeeper("Ana")
    lola = Veterinarian("Lola")

    print(ana.feed_animal(max, "eucalyptus"))
    print(ana.clean_enclosure(field))

    print(lola.check_health(lewis, "Injured tail", "moderate"))

    try:
        den.remove_animal(lewis)
    except ValueError as e:
        print("Blocked:", str(e))

    print(lola.resolve_issue(lewis))

    den.remove_animal(lewis)
    print("Lewis removed successfully.")


if __name__ == '__main__':
        main()