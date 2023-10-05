# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:43:57 2023

@author: kainen
"""

exList = ["A", "B", "C"]

print(enumerate(exList))

print(list(enumerate(exList)))

for i, value in enumerate(exList):
    print("{}번째 요소는 {}입니다.".format(i, value))