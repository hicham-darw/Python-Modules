class GardenManager:

    def __init__(self):
        self.plants = []
        self.tank_level = 20

    def add_plants(self, name, water, sun):

        try:
            if name is None:
                err = "Error adding plant: Plant name cannot be empty!"
                raise Exception(err)
            else:
                if (water > 10):
                    err = f"Error checking {name}: "
                    err += f"Water level {water} is too high (max 10)"
                    raise Exception(err)
                else:
                    if sun > 10:
                        err = f"Error checking {name}: "
                        err += f"sunlight level {sun} is too low (min 2)"
                        raise Exception(err)
        except Exception as e:
            print(e)
            return None
        new_plant = Plant(name, water, sun)
        self.plants.append(new_plant)
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        for plant in self.plants:
            plant.water += 5
            self.tank_level -= 5
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try:
            for plant in self.plants:
                if plant.water <= 10 and plant.sun >= 2:
                    msg = f"{plant.name}: healthy "
                    msg += f"(water: {plant.water}, sun: {plant.sun})"
                    print(msg)
                else:
                    if (plant.water > 10):
                        err = f"Error checking {plant.name}: Water level "
                        err += f"{plant.water} is too high (max 10)"
                        raise Exception(err)
                    else:
                        err = f"Error checking {plant.name}: "
                        err += f"sunlight level {plant.sun} is too low (min 2)"
                        raise Exception(err)
        except Exception as e:
            print(e)

    def check_tank(self):
        try:
            if self.tank_level <= 10:
                raise Exception("Caught GardenError: Not enough water in tank")
        except Exception as e:
            print(e)

    def fill_tank(self, level):
        try:
            if level <= 0:
                err = "Caught GardenError: "
                err += "cannot fill tank with negative value"
                raise Exception(err)
            else:
                self.tank_level += level
        except Exception as e:
            print(e)
        finally:
            print("System recovered and continuing...")


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
    garden.add_plants("lettuce", 10, 10)
    garden.add_plants(None, 2, 10)
    print("")
    print("Watering plants...")
    garden.water_plants()
    print("")
    print("Checking plant health...")
    garden.check_plant_health()
    print("")
    print("Testing error recovery...")
    garden.check_tank()
    garden.fill_tank(10)
    print("")
    print("Garden management system test complete!")
