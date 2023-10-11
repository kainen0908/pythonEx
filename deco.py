# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:17:51 2023

@author: kainen
"""

def test(function):
    def wrapper():
        print('인사가 시작되었습니다.')
        function()
        print('인사가 종료되었습니다.')
    return wrapper

@test
def hello():
    print('hello')
    
hello()