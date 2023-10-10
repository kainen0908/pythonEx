# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:20:43 2023

@author: kainen
"""

def modify(s):
    print(id(s))
    s += ' To You'
    print('msg=', s)
    print(id(s))
    
msg = "Happy Birthday"
print('msg=', msg)
print(id(msg))

modify(msg)
print('msg=', msg)
print(id(msg))