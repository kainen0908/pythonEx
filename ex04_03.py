# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:20:16 2023

@author: kainen
"""

limit = 10000
i = 1

sum_value = 0
while sum_value < 10000:
    sum_value += i
    i+=1
i-=1    
print ("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))
