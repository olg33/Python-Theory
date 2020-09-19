#!/usr/bin/env python3.8

user = {"username:": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def secure_function(func):
    if user["access_level"]== "admin":
        return func

get_admin_password = secure_function(func):
    if user["access_level"] == "admin":
        return func








