# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:09:48 2023

@author: kainen
"""

list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input('정수 입력 >'))
    print('{}번째 요소: {}'.format(number_input, list_number[number_input]))
    예외.발생()

# except Exception as exception:
#     print('type(exception): ', type(exception))
#     print('exception: ', exception)

except ValueError as exception:
    print('정수를 입력해 주세요')
    print('exception', exception)
    
except IndexError as exception:
    print('리스트의 인덱스를 벗어났어요!')
    print('exception', exception)
    
except Exception as exception:
    print('파악하지 못한 예외 발생!')
    print(type(exception), exception)