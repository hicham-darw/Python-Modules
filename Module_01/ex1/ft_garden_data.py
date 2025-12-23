class Plant:
    def __init__(self, name, h, a):
        self.name = name
        self.h = h
        self.a = a
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")


if __name__ == '__main__':
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
