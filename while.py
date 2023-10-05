# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:17:44 2023

@author: kainen
"""

list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)
    
print(list_test)


import time
number = 0
target_tick = time.time()+5
while time.time() < target_tick:
    number +=1

print(number)