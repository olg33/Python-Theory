#!/usr/bin/env python3

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (10,8,7,5,8))
student2 = Student("Rolf", (10,10,7,9,8))
print(student.name)
print(student.average())
print(student2.name)
print(student2.average())


