#!/usr/bin/env python3

movies = {"matrix", "Jaws", "ET"}
user = input("Enter recently watched movie : ")

if user in movies:
    print(f"I've watched {user} too")
else:
    print("I haven't watched that one yet")
