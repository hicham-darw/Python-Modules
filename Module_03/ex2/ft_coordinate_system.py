import math


def calculate_distance():
    a = tuple((0, 0, 0))
    x2, y2, z2 = a
    distance = math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2) + ((z2 - z) ** 2))
    return f"Distance between ({x2}, {y2}, {z2}) and ({x}, {y}, {z}): {distance:.2f}"


def parsing_coordinates(coordinates):
    
    lst = coordinates.split(',')
    try:
        x = int(lst[0])
        y = int(lst[1])
        z = int(lst[2])
    except Exception as e:
        print("Error parsing coordinates: ", end="")
        print(e)
        print(f"Error details - Type: {type(e).__name__}, Args: (\"{e}\",)")
    else:
        print(f"Parsed position: ({x}, {y}, {z})")
        t = (x, y, z)


def unpacking_demonstration():
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def create_tuple(str):
    lst = str.split(',')
    try:
        x = int(lst[0])
        y = int(lst[1])
        z = int(lst[2])
        t = tuple((x, y, z))
    except Exception:
        print("I typed ’abc’ instead of ’123’")
    else:
        return t


if __name__ == '__main__':
    print("=== Game Coordinate System ===")
    print("")
    t = create_tuple("10,20,5")
    x, y, z = t
    print("Position created ", end="")
    print(f"({x}, {y}, {z})")
    print(calculate_distance())
    print("")

    # parsing valid coordinates
    print("Parsing coordinates: \"3,4,0\"")
    t = create_tuple("3,4,0")
    x, y, z = t
    parsing_coordinates("3,4,0")
    print(calculate_distance())
    print("")

    # parsing invalid coordinates
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    parsing_coordinates("abc,def,ghi")
    print("")
    print("Unpacking demonstration:")
    unpacking_demonstration()
