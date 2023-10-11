# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:28:35 2023

@author: kainen
"""

from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()