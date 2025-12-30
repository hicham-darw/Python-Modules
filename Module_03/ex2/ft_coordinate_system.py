import math
import sys


def calculate_distance(coordinates):
    """
    this function calculate  distance between two points in 3D
    using tuple data-type Ordered and Unchangable
    args:
        a tuple (x, y, z)
    returns:
        string display both coordinates and distance between them
    """
    x1, y1, z1 = coordinates
    a = tuple((0, 0, 0))
    x2, y2, z2 = a
    distance = math.sqrt(
        ((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)
    )
    s = "Distance between"
    return f"{s} ({x2}, {y2}, {z2}) and ({x1}, {y1}, {z1}): {distance:.2f}"


def parsing_coordinates(coordinates):
    """
    parsing coordinates for invalid input
    Args:
        coordinates
    returns:
        a tuple if not any error or exception
    """
    lst = coordinates.split(',')
    try:
        x = float(lst[0])
        y = float(lst[1])
        z = float(lst[2])
    except Exception as e:
        print("Error parsing coordinates: ", end="")
        print(e)
        print(f"Error details - Type: {type(e).__name__}, Args: (\"{e}\",)")
        return None
    else:
        t = (x, y, z)
        print(f"Parsed position: ({t[0]}, {t[1]}, {t[2]})")
        return t


def unpacking_demonstration(coordinates):
    """
    function unpack a tuple and print values
    args:
        a tuple
    returns:
        None
    """
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    print("=== Game Coordinate System ===")
    print("")
    try:
        t = parsing_coordinates(sys.argv[1])
        print(f"Position created ({t[0]}, {t[1]}, {t[2]})")
        print(calculate_distance(t))
        print("")
    except Exception:
        print("invalid args. Usage: python3 ft_coordinate_system.py <coordinates>")
    else:
        print("Unpacking demonstration:")
        x, y, z = t
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates:  x={x}, y={y}, z={z}")

main()