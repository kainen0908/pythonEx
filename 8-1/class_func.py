# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:19:05 2023

@author: kainen
"""

class Student:
    count = 0
    students = []
    
    @classmethod
    def print(cls):
        print("------- 학생 목록 --------")
        print("이 름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------------------------")
    
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())



Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 79, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤이랑", 95, 98, 96, 98)
a = Student("윤명월", 67, 88, 92, 92)


Student.print()
a.print()
