# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:38:37 2023

@author: kainen
"""

from urllib import request

target = request.urlopen('https://google.com')
output = target.read()

print(output)