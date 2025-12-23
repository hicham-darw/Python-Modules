import math


def calculate_distance():
    a = (0, 0, 0)
    x2, y2, z2 = a
    distance = math.sqrt(((x - x2) ** 2) + ((y - y2) ** 2) + ((z - z2) ** 2))
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


print("=== Game Coordinate System ===")
print("")
tuple1 = (10, 20, 5)
x, y, z = tuple1
print("Position created ", end="")
print(f"({x}, {y}, {z})")
print(calculate_distance())
print("")

# parsing valid coordinates
print("Parsing coordinates: \"3,4,0\"")
parsing_coordinates("3,4,0")

# parsing invalid coordinates
print("Parsing invalid coordinates: \"abc,def,ghi\"")
parsing_coordinates("abc,def,ghi")
print("")
print("Unpacking demonstration:")
t = tuple((3, 4, 0))
lst = []
for elem in t:
    lst.append(elem)
print(f"Player at x={lst[0]}, y={lst[1]}, z={lst[2]}")
print(f"Coordinates: X={lst[0]}, Y={lst[1]}, Z={lst[2]}")
