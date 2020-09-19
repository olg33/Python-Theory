#!/usr/bin/env python3

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (10, 9, 8, 9, 7, 6)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob")
print(student.name)
print(student.average())


