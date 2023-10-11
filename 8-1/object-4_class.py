# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:36:26 2023

@author: kainen
"""

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 79, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤이랑", 95, 98, 96, 98),
    Student("윤명월", 67, 88, 92, 92)
]

print(students[0].name)
print(students[0].korean)

print("이  름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())