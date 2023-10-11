# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:40:30 2023

@author: kainen
"""

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")
        
class Chile(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")
    
child = Chile()
child.test()
print(child.value)