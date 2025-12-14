class SecurePlant:
    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age
        print("Plant created:", self.__name)

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return (self.__age)

    def set_height(self, update_height):
        if (update_height < 0):
            print("")
            invalid = "Invalid operation attempted: height "
            print(invalid, update_height, "cm [REJECTED]", sep="")
            print("Security: Negative height rejected")
            print("")
            current = "Current plant: " + self.__name + " ("
            print(current, self.__height, "cm, ", self.__age, " days)", sep="")
        else:
            self.__height += update_height
            print("Height updated: ", self.__height, "cm [OK]", sep="")

    def set_age(self, update_age):
        if (update_age < 0):
            print("")
            invalid = "Invalid operation attempted: height "
            print(invalid, update_age, "days [REJECTED]", sep="")
            print("Security: Negative age rejected")
            print("")
            current = "Current plant: " + self.__name + " ("
            print(current, self.__height, "cm, ", self.__age, " days)", sep="")
        else:
            self.__age += update_age
            print("Age updated: ", self.__age, " days [OK]", sep="")


if (__name__ == "__main__"):
    print("=== Garden Security System ===")
    plant_rose = SecurePlant("Rose", 20, 29)
    plant_rose.set_height(5)
    plant_rose.set_age(1)
    plant_rose.set_height(-5)
