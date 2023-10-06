# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:38:05 2023

@author: kainen
"""

# =============================================================================
# def power(item):
#     return item*item
# 
# def under_3(item):
#     return item < 3
# =============================================================================

power =  lambda x: x*x
under_3 = lambda x: x<3

list_input_a=[1,2,3,4,5]

output_a = map(power, list_input_a)
print(output_a)

print(list(output_a))

output_b = filter(under_3, list_input_a)

print(output_b)
print(list(output_b))