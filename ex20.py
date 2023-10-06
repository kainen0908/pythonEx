# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:16:12 2023

@author: kainen
"""

code = input('염기 서열을 입력해주세요: ')

dic={}

for i in range(len(code)//3):
    key = code[3*i:3*i+3]
    if key in dic:
        dic[key] +=1
    else:
        dic[key] =1
print(dic)