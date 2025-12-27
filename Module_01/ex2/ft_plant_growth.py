class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.h = height
        self.a = age

    def grow(self):
        self.h += 6
        self.age()

    def age(self):
        self.a += 6

    def get_info(self):
        print(self.name, ": ", self.h, "cm, ", self.a, " days old", sep="")

    def week_of_growth(self):
        print("Growth this week: +6cm")


if __name__ == '__main__':
    print("=== Day 1 ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.get_info()
    print("=== Day 7 ===")
    plant1.grow()
    plant1.get_info()
    plant1.week_of_growth()
    plant1.grow()
    plant1.get_info()
