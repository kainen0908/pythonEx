# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:31:03 2023

@author: kainen
"""

import test_module as test

print('메인의 __name__ 출력')
print(__name__)
print()

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

