# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:17:53 2023

@author: kainen
"""
dictionary = {
    1: 1,
    2: 1
    }

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

    
for i in range(1,1000):
    counter = 0
    print(i, fibonacci(i))