# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:29:46 2023

@author: kainen
"""

numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

print("reversed_numbers : ", r_num)

while True:
    try:
        val = next(r_num)
        print(val)
    except:
        break