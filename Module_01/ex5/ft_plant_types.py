class Plant:
    def __init__(self, name, height, age):
        self.n = name
        self.h = height
        self.a = age


class Flower(Plant):
    def __init__(self, name, height, age, color, is_bloom):
        super().__init__(name, height, age)
        self.color = color
        self.blm = is_bloom
        type_flower = self.n + " (Flower): "
        her_color = " days, " + self.color + " color"
        print(type_flower, self.h, "cm, ", self.a, her_color, sep="")

    def bloom(self):
        if (self.blm):
            print(self.n, " is blooming bueatifully!", sep="")
        else:
            print(self.n, " is not blooming yet!", sep="")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.td = trunk_diameter
        self.shade = shade
        typ = self.n + " (Tree): "
        day = " days, "
        print(typ, self.h, "cm, ", self.a, day, self.td, "cm diameter", sep="")

    def produce_shade(self):
        if (self.shade):
            print(self.n, "provides", self.shade, "square meters of shade")
        else:
            print(self.n, "provides", self.shade, "square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvs = harvest_season
        self.nut_val = nutritional_value
        typ = self.n + " (Vegetable): "
        day = " days, "
        print(typ, self.h, "cm, ", self.a, day, self.harvs, " harvest", sep="")
        print(self.n, "is rich in", self.nut_val)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")

    fl = Flower("Rose", 25, 30, "red", 1)
    fl.bloom()
    print("")
    tr = Tree("Oak", 500, 1825, 50, 78)
    tr.produce_shade()
    print("")
    Veg = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
