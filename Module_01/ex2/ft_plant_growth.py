#!/bin/usr/env python3

class Plant:
    def __init__(self, name, height, age):
        self.p_name = name
        self.p_height = height
        self.p_age = age
        print(self.p_name, ": ", self.p_height, "cm, ", self.p_age, " days old", sep="")

    def grow(self, day=1):
        self.p_height += (day - 1)

    def age(self, age=1):
        self.p_age += age - 1
    
    def get_info(self, days=0):
        print(self.p_name, ": ", self.p_height, "cm, ", self.p_age, " days old", sep="")
        if days == 7:
            print("Growth this week: ", "+", (days - 1), "cm", sep="")
if __name__ == "__main__":
    print("=== Day 1 ===")
    plant1 = Plant("Rose",25,30)
    print("=== Day 7 ===")
    growth = 7
    plant1.age(growth)
    plant1.grow(growth)
    plant1.get_info(7)
