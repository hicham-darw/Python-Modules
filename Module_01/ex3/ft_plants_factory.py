counter_plants = 0


class Plant:
    def __init__(self, name, start_height, start_age):
        global counter_plants
        self.name = name
        self.h = start_height
        self.a = start_age
        counter_plants += 1
        created = "Created: " + self.name
        print(created, " (", self.h, "cm, ", self.a, " days)", sep="")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_rose = Plant("Rose", 25, 30)
    plant_oak = Plant("Oak", 200, 365)
    plant_cactus = Plant("Cactus", 5, 90)
    plant_sunflower = Plant("Sunflower", 80, 45)
    plant_fern = Plant("Fern", 15, 120)
    print("")
    print("Total plants created:", counter_plants)
