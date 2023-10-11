# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:47:21 2023

@author: kainen
"""

class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("### 내가 만든 오류가 생성됨! ###")
    def __str__(self):
        print("Exception의 str: ", super().__str__())
        return "오류발생"
    
raise CustomException()