class GardenManager:
    def __init__(self)
        self.plants = {}

    def creat_plant(self, plant_type):
        self.plants.appaend(plant_type)
    
    def remove_plant(self, plant_name, plant_height, plant_age):
        self.plant.remove(plant_type)
    

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def say_hello(self):
        print(f"hello {self.name}")

class FloweringPlant(Plant):
    def __init__(self, name, height, age, flowering):
        super().__init__(name, height, age)
        self.flowering = flowering
        print(help(type(self)))


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, bloom, price):
        self.price = price


print("=== Garden Management System Demo ===")
alice = GardenManager()

