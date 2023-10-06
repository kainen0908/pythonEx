# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:06:19 2023

@author: kainen
"""

def mul(*values):
    a=1
    for i in values:
        a *=i
    return a 

print(mul(5,7,9,10))