# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:47:17 2023

@author: kainen
"""
# 반복문
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
    

# 역반복문
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))