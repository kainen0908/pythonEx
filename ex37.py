# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:45:13 2023

@author: kainen
"""
'''
file = open('basic.txt', 'w')

file.write('Hello Python')

file.close()
'''

with open('basic.txt', 'w') as file:
    file.write('Hi')