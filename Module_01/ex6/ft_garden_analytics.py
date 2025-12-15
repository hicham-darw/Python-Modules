class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom
        print(help(type(self)))

rose = Flower("rose", 10, 10, "red", "True")

