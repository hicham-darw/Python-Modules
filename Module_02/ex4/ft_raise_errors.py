def check_plant_health(plant_name, water_level, sunlight_hours):
    """ This function check plant health with valid input
        if not valid raise an exception

        Args:
            plant_name (str): name of plant not None
            water_level (int): water level not higher than max
            sunlight_hours (int): sunlight hours not lower than 2 hours

        Returns:
            None.
    """
    try:
        if plant_name is None:

            raise ValueError("Error: Plant name cannot be empty!")
        else:
            if (water_level > 10):
                e = f"Error: Water level {water_level} is too high (max 10)"
                raise ValueError(e)
            else:
                if (sunlight_hours < 2):
                    err = "Error: Sunlight hours"
                    e = f"{err} {sunlight_hours} is too low (min 2)"
                    raise ValueError(e)
                else:
                    print(f"Plant {plant_name} is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks():
    """ This function test plant with:
    good values, empty plant name, bad water, bad sunlight hours

        Args:
            None.

        Returns:
            None.
    """
    print("=== Garden Plant Health Checker ===")
    print("")
    print("Testing good values...")
    check_plant_health('tomato', 10, 6)
    print("")
    print("Testing empty plant name...")
    check_plant_health(None, 10, 6)
    print("")
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 2)
    print("")
    print("Testing bad sunlight hours...")
    check_plant_health('tomato', 10, 0)
    print("")
    print("All error raising tests completed!")


test_plant_checks()
