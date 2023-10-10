# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:42:25 2023

@author: kainen
"""

from operator import itemgetter

books = [{
    '제목': '혼자 공부하는 파이썬',
    '가격': 18000
    }, {
    '제목': '혼자 공부하는 머신러닝 + 딥러닝',
    '가격': 26000
    }, {
    '제목': '혼자 공부하는 자바스크립트',
    '가격': 24000    
}]
        
print('# 가장 저렴한 책')
print(min(books, key=itemgetter('가격')))
print()

print('# 가장 비싼 책')
print(max(books, key=itemgetter('가격')))