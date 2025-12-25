def water_plants(plant_list):
    """ This function check if list of plants is valid or not
        and do not crash program by invalid input

        Args:
            plant_list: [list].

        Returns:
            None.
    """
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception
            else:
                print(f"Watering {plant}")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """ This function test valid input and invalid input
        and  should display is closing watering and cleaning up

        Args:
            None.

        Returns:
            None.
    """
    print("=== Garden Watering System ===")
    print("")
    print("Testing normal watering...")
    plant_list = ['tomato', 'lettuce', 'carrots']
    print("Opening watering system")
    water_plants(plant_list)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    print("Opening watering system")
    plant_list = ['tomato', None]
    water_plants(plant_list)
    print("")
    print("Cleanup always happens, even with errors!")


test_watering_system()
