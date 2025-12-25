x = 0


def garden_operations():
    """ This function handle multi exception on each call by global var x.

        Args:
            None.

        Returns:
            None.
                                                                        """
    global x
    if x == 0:
        print("Testing ValueError...")
        try:
            x = int('abc')
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif x == 1:
        print("Testing ZeroDivisionError...")
        try:
            res = 10
            res /= 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif x == 2:
        print("Testing FileNotFoundError...")
        try:
            raise FileNotFoundError
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
    elif x == 3:
        print("Testing KeyError...")
        try:
            d = {1: "This is me", 2: "this is again me"}
            print(d['Darwin'])
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")
    else:
        print("Testing multiple errors together...")
        try:
            x = 1 / 0
            raise FileNotFoundError
        except (FileNotFoundError, ZeroDivisionError):
            print("Caught an error, but program continues!")
    x += 1


def test_error_types():
    """ This function call function above each time to display errors.

    Args:
        None.

    Returns:
        None.
                                                                    """
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    print("")
    garden_operations()
    print("")
    garden_operations()
    print("")
    garden_operations()
    print("")
    garden_operations()
    print("")
    print("All error types tested successfully!")


test_error_types()
