# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:02:52 2023

@author: kainen
"""

def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output

print ('A.', sum_all(0, 100, 10))
print ('B.', sum_all(end=100))
print ('C.', sum_all(end=100, step=2))