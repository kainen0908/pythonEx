# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:47:42 2023

@author: kainen
"""

# 파괴적
a = [52, 273, 103, 32, 57, 272]

a.sort()

a.sort(reverse=True)


# 비파괴적
a = [52, 273, 103, 32, 57, 272]
b = sorted(a)

b = sorted(a, reverse=True)