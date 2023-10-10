# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:55:37 2023

@author: kainen
"""

def modify(n):
    print(id(n))
    n = n + 1
    print('n=', n)
    print(id(n))
    
k = 10
print('k=', k)
print(id(k))

modify(k)
print('k=', k)
print(id(k))