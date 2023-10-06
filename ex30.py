# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:41:27 2023

@author: kainen
"""

def flatten(data):
    output=[]
    
    for item in data:
        if type(item) ==list:
            output += flatten(item)
        else:
            output.append(item)
    
    return output


example = [[1,2,3],[4,[5,6]],7,[8,9]]
print('원본: ' , example)
print('변환: ' , flatten(example))