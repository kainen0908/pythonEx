# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:48:44 2023

@author: kainen
"""

a=[1,2,3,4,1,2,3,1,4,1,2,3]

dic={}

for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] +=1
    else:
        dic[a[i]] =1
        
print(dic)
print(a, '.에서\n', '사용된 숫자의 종류는 {}개 입니다.'.format(len(dic)), sep='')