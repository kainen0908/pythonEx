# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:11:40 2023

@author: kainen
"""

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    def get_circumferenc(self):
        return 2 * math.pi * self.__radius

    def get_circle_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <=0:
            raise TypeError("반지름은 양수만 가능합니다.")
        self.__radius = value
        

circle = Circle(10)
print("둘레: ", circle.get_circumferenc())
print("넓이: ", circle.get_circle_area())
circle.__radius = 2
print(circle.__radius)
circle.radius = 4
print(circle.radius)
print(circle.get_radius())