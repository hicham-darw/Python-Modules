x = 0

def test_error_types():
    global x
    if x == 0:
        print("=== Garden Error Types Demo ===")
        print("")
        print("Testing ValueError...")
        try:
            x = int('abc')
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
            print("")
    elif x == 1:
        print("Testing ZeroDivisionError...")
        try :
            div = 0
            res = 10 / div
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
            print("")
    elif x == 2:
        print("Testing FileNotFoundError...")
        try:
            raise FileNotFoundError
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
            print("")
    elif x == 3:
        print("Testing KeyError...")
        try:
            d = {1: "This is me", 2: "this is again me"}
            print(d['Darwin'])
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")
            print("")
    else:
        print("Testing multiple errors together...")
        try:
            x = 1 / 0
            raise FileNotFoundError
        except (FileNotFoundError, ZeroDivisionError):
            print("Caught an error, but program continues!")
            print("")
            print("All error types tested successfully!")
    x += 1

def garden_operations():
    pass

if __name__ == '__main__':
    test_error_types()
    test_error_types()
    test_error_types()
    test_error_types()
    test_error_types()