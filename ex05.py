# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:26:19 2023

@author: kainen
"""

# 1
numbers = [ 1,2,3,4,5,6,7,8,9,1,2,4,5,6,7,4,3,9]
counter = {}

for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print(counter)

# 2
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor":"풀플레이트"
        },
    "skill": ["베기", "세게베기", "아주 세게 베기"]
    }

for key in character:
    val = character[key]
    if type(val) is str:
        print(key, ":", val)
    elif type(val) is list:
        for el in val:
            print(key, ":", el)
    elif type(val) is dict:
        for subkey in val:
            print(subkey, ":", val[subkey])
