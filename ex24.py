# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:36:02 2023

@author: kainen
"""

def print_n_times(value, n=2):
    for i in range(n):
        print(value)
    
print_n_times("안녕", 2)

print("=======================")

def print_n_times2(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
    
print_n_times2("안녕",'즐거운', '파이썬', 3)

print("=======================")