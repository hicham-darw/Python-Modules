class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height + "cm,"
		self.age = age 
		print(name + ":", height, age, "days old")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")
	plant1 = Plant("Rose", "25cm,", 30)
	plant2 = Plant("Sunflower","80cm,", 45)
	plant3 = Plant("Cactus", "15cm,", 120)

