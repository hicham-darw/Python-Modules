class GardenError(Exception):
    def __init__(self, msg="Garden Error!"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, name, msg=" plant is wilting!"):
        self.name = name
        super().__init__("The " + self.name + msg)

class WaterError(GardenError):
    def __init__(self, msg="Not enough water in the tank!"):
        super().__init__(msg)


def custom_error():
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try :
        raise PlantError('tomato')
    except PlantError as e:
        print("Caught PlantError: ", end="")
        print(e)
        print("")
    print("Testing WaterError...")
    try :
        raise WaterError()
    except WaterError as e:
        print("Caught WaterError: ", end="")
        print(e)
        print("")
    print("Testing catching all garden errors...")
    try :
       raise PlantError('tomato')
    except PlantError as e:
       print("Caught a garden error: ", end="")
       print(e)
    try :
       raise WaterError()
    except WaterError as e:
       print("Caught a garden error: ", end="")
       print(e)
       print("")
    print("All custom error types work correctly!")


custom_error()
