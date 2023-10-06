# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:50:05 2023

@author: kainen
"""

min = 2
max = 100
all = 100

memo = {}

def prob(n, s):
    key = str([n, s])
    
    if key in memo:
        return memo[key]
    if n < 0:
        return 0
    if n == 0:
        return 1
    
      