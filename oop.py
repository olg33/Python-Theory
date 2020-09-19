#!/usr/bin/env python3

class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (10, 9, 8, 9, 7, 6)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(Student.average(student))


