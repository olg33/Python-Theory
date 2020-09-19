#!/usr/bin/env python3
student_attendance = {"Rolf":96, "Bob": 80, "Sue": 100}

for student, attendance in student_attendance.items():
    #f means Formated string literals
    print(f"{student}: {attendance}")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


person = ("Bob", 42, "mECHANIC")
name, _ , profession = person
print(name, profession)
