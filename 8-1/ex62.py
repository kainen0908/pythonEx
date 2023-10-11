# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:15:24 2023

@author: kainen
"""

class Student:
    def study(self):
        print("공부 합니다.")

class Teacher:
    def teach(self):
        print("가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()