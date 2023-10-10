# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:25:36 2023

@author: kainen
"""

def modify(li):
    print(id(li))
    li += [100, 200]
    print(list)
    print(id(li))

list = [1,2,3,4,5]
print(list)
print(id(list))

modify(list)
print(list)
print(id(list))