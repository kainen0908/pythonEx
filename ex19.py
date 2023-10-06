# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:11:21 2023

@author: kainen
"""

code = input('염기 서열을 입력해주세요: ')

dic={}

for i in range(len(code)):
    if code[i] in dic:
        dic[code[i]] +=1
    else:
        dic[code[i]] =1
print(dic)
for c, cnt in dic.items():
    print('{}의 개수: {}'.format(c,cnt))