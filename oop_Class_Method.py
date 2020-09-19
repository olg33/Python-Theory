#!/usr/bin/env python3

class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

ClassTest.class_method()



