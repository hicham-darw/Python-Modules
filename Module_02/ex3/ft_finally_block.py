def water_plants(plant_list):
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


if __name__ == '__main__':
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()
