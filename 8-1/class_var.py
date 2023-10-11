# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:19:05 2023

@author: kainen
"""

class Student:
    count = 0
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
        Student.count += 1
        
    # 소멸자
    def __del__(self):
        print("{} - 소멸되었습니다.".format(self.name))
    

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 79, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤이랑", 95, 98, 96, 98),
    Student("윤명월", 67, 88, 92, 92)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
print("현재 생성된 총 학생 수는 {}명입니다.".format(students[0].count))
