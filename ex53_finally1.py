# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:34:38 2023

@author: kainen
"""

try:
    file = open('info.txt', 'w')
    예외.발생()
except:
    print('오류 발생')
finally:
    file.close()

print('file.closed:', file.closed)