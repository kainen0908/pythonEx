# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:28:23 2023

@author: kainen
"""


import math

class Circle:
    
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자로!")
        self.__radius = value


circle = Circle(10)
print(circle.radius)
try:
    circle.__radius = 2
    print(circle.__radius)
    print()
    circle.radius = -10
except TypeError as e:
    print(e)