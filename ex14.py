# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:12:37 2023

@author: kainen
"""

# array = [i*i for i in range(0, 20, 2)]

# print(array)

array = ['사과', '자두', '초콜릿','바나나','체리']
output = [fruit for fruit in array if fruit !='초콜릿']

print(output)