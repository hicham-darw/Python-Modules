class GardenError(Exception):
    """ This class enherit from exception class.
        attributes:
                None.
        Methods:
            __init__(): constructor class for display error msg for garden.
            super().__init_(): function is used to call methods from superclass
            inside childclass.
    """
    def __init__(self, msg="Garden Error!"):
        super().__init__(msg)


class PlantError(GardenError):
    """ This class enherit from class GardenError

        Attributes:
                None.
        Methods:
            __init_(): constructor class for display Error msg plant.
            super().__init_(): function is used to call methods from superclass
            inside childclass.

    """
    def __init__(self, name, msg=" plant is wilting!"):
        self.name = name
        super().__init__("The " + self.name + msg)


class WaterError(GardenError):
    """ This class enherit from class GardenError

        Attributes:
                None.
        Methods:
            __init_(): constructor class for display Error msg for water.
            super().__init_(): function is used to call methods from superclass
            inside childclass.

    """
    def __init__(self, msg="Not enough water in the tank!"):
        super().__init__(msg)


def custom_error():
    """ This Function only test my custom errors

        Args:
                None.
        Return:
                None.
    """
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        raise PlantError('tomato')
    except PlantError as e:
        print("Caught PlantError: ", end="")
        print(e)
        print("")
    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print("Caught WaterError: ", end="")
        print(e)
        print("")
    print("Testing catching all garden errors...")
    try:
        raise PlantError('tomato')
    except PlantError as e:
        print("Caught a garden error: ", end="")
        print(e)
    try:
        raise WaterError()
    except WaterError as e:
        print("Caught a garden error: ", end="")
        print(e)
        print("")
    print("All custom error types work correctly!")


custom_error()
