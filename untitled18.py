# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:37:30 2023

@author: kainen
"""

max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    
    if(max_value < i*j):
        a=i
        b=j
        max_value = i * j
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))