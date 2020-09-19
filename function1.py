#!/usr/bin/env python3
 
def user_age():
     age = int(input("Enter age: "))
     age_sec = age * 365 * 24 * 60 * 60
     print(f"Your age in seconds is {age_sec}.")

user_age()

