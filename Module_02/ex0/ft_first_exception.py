def check_temperature(temp_str):
    print("Testing temperature:", temp_str)
    try:
        res = int(temp_str)
    except ValueError:
        print("Error: '" + temp_str + "' is not a valid number")
    else:
        if res < 0:
            print("Error: ", temp_str, "°C is too cold for plants (min 0°C)")
        elif res > 40:
            print("Error: ", temp_str, "°C is too hot for plants (max 40°C)")
        else:
            print("Temperature", temp_str, "°C is perfect for plant!")

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print("")
    check_temperature("25")
    print("")
    check_temperature("abc")
    print("")
    check_temperature("100")
    print("")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash")
        
test_temperature_input()