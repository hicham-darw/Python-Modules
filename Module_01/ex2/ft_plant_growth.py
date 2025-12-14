#!/bin/usr/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.h = height
        self.a = age
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")

    def grow(self, day=1):
        self.h += (day - 1)

    def age(self, age=1):
        self.a += age - 1

    def get_info(self, days=0):
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")
        if days == 7:
            print("Growth this week: ", "+", (days - 1), "cm", sep="")


if __name__ == "__main__":
    print("=== Day 1 ===")
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 7 ===")
    growth = 7
    plant1.age(growth)
    plant1.grow(growth)
    plant1.get_info(7)
