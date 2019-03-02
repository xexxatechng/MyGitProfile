# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:18:41 2019

@author: HP
"""

"""
15-7. Two D8s: Create a simulation showing what happens if you roll two eightsided
dice 1000 times. Increase the number of rolls gradually until you start to
see the limits of your system’s capabilities."""


from random import randint

"""create class Dice"""
class Dice():
    def __init__ (self, sides=8):
        """Attribute/variable declaration"""
        self.sides = sides
        
    def roller(self):
        """Randomly roll the dice to generate data between 1 and 8"""
        return randint(1, self.sides)
