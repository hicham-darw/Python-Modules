#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age 
		print(self.name, ": ", self.height, "cm, ", self.age, " days old", sep="")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")
	plant1 = Plant("Rose",25,30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)

