class GardenManager:

    def __init__(self):
        self.plants = []
        
    def add_plants(self, name, water, sun):
        
        try:
            if name is None:
                raise ValueError("Error adding plant: Plant name cannot be empty!")
            else:
                if (water > 10):
                    raise ValueError(f"Error checking {name}: Water level {water} is too high (max 10)")
                else:
                    if sun > 10:
                        raise ValueError(f"Error checking {name}: Water level {sun} is too high (max 10)")
        except ValueError as e:
            print(e)
            return None
        new_plant = Plant(name, water, sun)
        self.plants.append(new_plant)
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        for plant in self.plants:
            plant.water += 5
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try :
            for plant in self.plants:
                if plant.water <= 10 and plant.sun >= 2:
                    print("{self.name}: healthy (water: self.water, sun: {self.sun})")
                else:
                    if (plant.water > 10):
                        raise Exception("Error checking {plant.name}: Water level {plant.water} is too high (max 10)")
                    else:
                        raise Exception("Error checking {plant.name}: Water level {plant.sun} is too high (min 2)")
        except Exception as e:
            print(e)


class Plant(GardenManager):
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

if __name__ == '__main__':
    print("=== Garden Management System ===")
    print("")
    garden = GardenManager()
    print("Adding plants to garden...")
    garden.add_plants("tomato", 2, 10)
    garden.add_plants("lettuce", 2, 10)
    garden.add_plants(None, 2, 10)
    print("")
    print("Watering plants...")
    garden.water_plants()
    print("")
    print("Checking plant health...")

    

