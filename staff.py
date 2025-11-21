'''
File: staff.py
Description: A brief description of this Python module.
Author: Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from enclosure import Enclosure


class Staff:
    #Base class for all staff.

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return self.name + " (" + self.role + ")"


class Zookeeper(Staff):
    #Zookeeper responsible for feeding and cleaning.

    def __init__(self, name):
        Staff.__init__(self, name, "zookeeper")

    def feed_animal(self, animal, food):
        return "[" + self.name + "] " + animal.eat(food)

    def clean_enclosure(self, enclosure):
        return "[" + self.name + "] " + enclosure.clean()


class Veterinarian(Staff):
    #Veterinarian responsible for health checks.

    def __init__(self, name):
        Staff.__init__(self, name, "veterinarian")

    def check_health(self, animal, description, severity):
        animal.report_health_issues(description)
        return "[" + self.name + "] recorded issue for " + animal.name + " (" + severity + ")"

    def resolve_issue(self, animal):
        animal.resolve_health_issues()
        return "[" + self.name + "] resolved issue for " + animal.name

