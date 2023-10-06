# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:22:25 2023

@author: kainen
"""

a = [1,2,[3,4],5,[6,7],[8,9]]

b=[]

for el in a:
    if type(el) == list:
        for v in el:
            b.append(v)
    else:
        b.append(el)
        
print(a, '를 평탄화하면\n', b, '입니다.', sep='')