'''
File: main.py
Description: Script showing how the zoo systems works.
Author: Amy Lukan
ID: 110458803
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
    max_koala = Mammal("Max", "Koala", 2, ["eucalyptus"], "temperate")
    oscar_emu = Bird("Oscar", "Emu", 4, ["pellets"], "grassland")
    lewis_lizard = Reptile("Lewis", "Blue-tongued Lizard", 3, ["insects"], "terrarium")

    grove = Enclosure("Koala Grove", 800, "temperate")
    field = Enclosure("Emu Field", 1200, "grassland")
    den = Enclosure("Lizard Den", 200, "terrarium")

    grove.add_animal(max_koala)
    field.add_animal(oscar_emu)
    den.add_animal(lewis_lizard)

    print("Animals and Enclosures created.")

    print("=== Zoo Operations ===")
# Staff actions: feeding, cleaning, health checks & movement rules

    ana = Zookeeper("Ana")
    lola = Veterinarian("Lola")

    print(ana.feed_animal(max_koala, "eucalyptus"))
    print(ana.clean_enclosure(field))

    print(lola.check_health(lewis_lizard, "Injured tail", "moderate"))

    try:
        den.remove_animal(lewis_lizard)
    except ValueError as e:
        print("Blocked:", str(e))

    print(lola.resolve_issue(lewis_lizard))

    den.remove_animal(lewis_lizard)
    print("Lewis removed successfully.")


if __name__ == '__main__':
        main()