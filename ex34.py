# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:31:31 2023

@author: kainen
"""

def call_10_times(func):
    for i in range(10):
        func()
        
def print_hello():
    print('안녕')
    
call_10_times(print_hello)

call_10_times((lambda : "hello"))