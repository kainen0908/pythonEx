# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:06:12 2023

@author: kainen
"""

class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성".format(self.name))
        
    def __del__(self):
        print("{} - 소멸".format(self.name))
        
Test("A")
Test("B")
Test("C")