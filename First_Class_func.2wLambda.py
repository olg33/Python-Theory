#!/usr/bin/env python3.8

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Oscar Lopez", "age": 24},
    {"name": "Anne Pun", "age": 34},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rolf Smith", lambda friend: friend["name"]))









