# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:47:27 2023

@author: kainen
"""
cnt = 0


def hanoi_tower(n, org, tmp, to):
    global cnt
    if(n == 1):
        print('원판 1 을', org, '에서', to, '로 옮긴다.')
        cnt += 1
    else:
        hanoi_tower(n-1, org, to, tmp)
        print('원판', n, '을', org, '에서', to, '로 옮긴다.')
        cnt += 1
        hanoi_tower(n-1, tmp, org, to)

hanoi_tower(10, 'A', 'B', 'C')
print(cnt)