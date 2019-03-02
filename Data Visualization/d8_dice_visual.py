# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:28:25 2019

@author: HP
"""

from dice import Dice

"""Create an object to call the Dice class"""
dice_1 = Dice()
dice_2 = Dice()

results = []
for roll in range(1001):
    result = dice_1.roller() + dice_2.roller()
    results.append(result)
print(results)
    
frequencies = []
max_sides = dice_1.sides + dice_2.sides
for value in range(2, max_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
    
    
import matplotlib.pyplot as plt

D8 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
frequencies = [13, 36, 44, 61, 69, 96, 112, 115, 118, 102, 70, 58, 53, 37, 16]

plt.bar(D8, frequencies)

#plt.title("Data from 8 sided dice ")
plt.xlabel("D8 Dice", fontsize=10)
plt.ylabel("Frequencies of occurence", fontsize=10)


plt.show()
