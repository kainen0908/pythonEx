# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:32:38 2023

@author: kainen
"""

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
        
print_n_times(4 ,'hi','test', 'ex','code')