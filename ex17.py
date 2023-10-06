# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:35:07 2023

@author: kainen
"""

output = [i for i in range(2, 99) if '{:b}'.format(i).count('0') ==1]


for i in output:
    print('{}:{:b}'.format(i, i))
print('합계: ', sum(output))
