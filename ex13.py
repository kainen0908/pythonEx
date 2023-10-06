# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:05:32 2023

@author: kainen
"""

example_dictionary = {
    "kA": "vA",
    "kB": "vB",
    "kC": "vC" 
    }

print("items(): ", example_dictionary.items())
print()

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))