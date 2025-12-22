#!/bin/usr/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.h = height
        self.a = age
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")

    def grow(self):
        self.h += 6

    def age(self):
        self.a += 6

    def get_info(self):
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")

    def week_of_growth(self):
        self.grow()
        self.age()
        self.get_info()
        print("Growth this week: ", "+", "6cm", sep="")


if __name__ == "__main__":
    print("=== Day 1 ===")
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 7 ===")
    plant1.week_of_growth()
