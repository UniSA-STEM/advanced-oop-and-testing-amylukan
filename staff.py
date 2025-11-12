'''
File: staff.py
Description: A brief description of this Python module.
Author: Amy Lukan
ID:
Username: LUKAY008
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"

