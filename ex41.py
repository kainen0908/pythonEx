# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:26:45 2023

@author: kainen
"""

def test():
    print('함수가 호출되었습니다.')
    yield 'test'
    
print('A지점 통과')
test()

print('B지점 통과')
test()

print(test())