# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:08:54 2023

@author: kainen
"""

import random

hanguls = list("가나다라마바사아자차카타파하")

with open('info.txt', 'w') as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        
        file.write('{}, {}, {}\n'.format(name, weight, height))