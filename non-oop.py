#!/usr/bin/env python3

student = {"name": "Rolf" , "grades": (9,7,10,9,8) }

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

