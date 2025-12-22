class Plant:
    total_plants = 0

    def __init__(self, name, start_height, start_age):
        self.name = name
        self.h = start_height
        self.a = start_age
        Plant.total_plants += 1
        print(f"Created: {self.name} ({start_height}cm, {start_age} days)")


print("=== Plant Factory Output ===")
plant_rose = Plant("Rose", 25, 30)
plant_oak = Plant("Oak", 200, 365)
plant_cactus = Plant("Cactus", 5, 90)
plant_sunflower = Plant("Sunflower", 80, 45)
plant_fern = Plant("Fern", 15, 120)
print("")
print("Total plants created:", Plant.total_plants)
