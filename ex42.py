# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:29:35 2023

@author: kainen
"""

def test():
    print('A')
    yield 1
    print('B')
    yield 2
    print('C')
    
output = test()

print('D')
a = next(output)
print(a)

print('E')
b = next(output)
print(b)

# error
next(output)