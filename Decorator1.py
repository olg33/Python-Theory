#!/usr/bin/env python3.8
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

#print(ordinary())

# Let's decorate this ordinary function

pretty = make_pretty(ordinary)
print(pretty)









