# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:38:00 2023

@author: kainen
"""

def test():
    print('첫줄')
    try:
        print('try실행')
        return
        print('return 뒤')
    except:
        print('exception 실행')
    else:
        print('else 실행')
    finally:
        print('finally 실행')
    print('test() 마지막줄')
    
    
test()