#!/usr/bin/env python3

name = "Bob"
print(f"Hello, {name}")

Name = "Rolf"
greeting = "Hello, {}"
W_Name = greeting.format(Name)
print(W_Name)

long_Phrase = "Hello, {}. Today is {}."
formatted = long_Phrase.format("Rolf", "Monday")
print(formatted)
