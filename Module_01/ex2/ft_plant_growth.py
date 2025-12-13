from ex1 import Plant

# class should be in ex1
class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age 

	def grow(height):
			self.height += height

	def age(self, day):
		return	self.age

	def get_info(self, day):
		self.age += (day - 1)
		self.height += (day - 1)
		print(self.name, ": ", self.height, "cm, ", self.age, " days old", sep="")
		if (day == 7):
			print("Growth this week: +", (day - 1), "cm", sep="")
			tmt = day - 1

if __name__ == "__main__":
	print("=== Day 1 ===")
	plant1 = Plant("Rose",25,30)
	plant1.get_info(1)
	print("=== Day 7 ===")
	plant1.get_info(7)
