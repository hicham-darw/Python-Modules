class GardenManager:
    height_validation = 0
    managers = []

    def __init__(self, name):
        self.plants = []
        self.name = name
        GardenManager.managers.append(self)
        self.score = 0
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0
        self.total_growth = 0

    def add_plant(self, plant):
        self.score += 70
        if (plant.height < 10):
            GardenManager.height_validation -= 1
        self.plants.append(plant)
        if (plant.type == "Tree"):
            self.regular += 1
        elif (plant.type == "FloweringPlant"):
            self.flowering += 1
        else:
            self.prize_flowers += 1

        if (plant.type == "Tree"):
            added_tree = "Added " + plant.name + " " + plant.type
            print(added_tree, " to ", self.name, "'s garden", sep="")
        else:
            added_flower = "Added " + plant.name + " to "
            print(added_flower, self.name, "'s garden", sep="")

# deleting plant or mort
    def delete_plant(self, plant):
        self.plants.remove(plant)

    def watering(self):
        self.score += 8
        print(self.name, "is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.total_growth += 1
        print("")

    def garden_report(self):
        print("Plants in garden:")
        for plant in self.plants:
            if plant.type == "Tree":
                tree = "- " + plant.name + " " + plant.type + ": "
                print(tree, plant.height, "cm", sep="")
            elif plant.type == "FloweringPlant":
                fname = "- " + plant.name + ": "
                fcolor = plant.color + " flowers (blooming) "
                print(fname, plant.height, "cm, ", fcolor, sep="")
            else:
                pfname = "- " + plant.name + ": "
                pfcolor = "cm, " + plant.color + " flowers (blooming), "
                pf = "Prize points"
                print(pfname, plant.height, pfcolor, pf, plant.prize, sep="")
        print("")
        total_added = self.regular + self.flowering + self.prize_flowers
        p_a = "Plants added: "
        t_g = ", Total growth: "
        print(p_a, total_added, t_g, self.total_growth, "cm", sep="")
        pt = "Plant types:"
        rg = "regular,"
        fl = "flowering,"
        pf = "prize flowers"
        print(pt, self.regular, rg, self.flowering, fl, self.prize_flowers, pf)
        print("")

    @classmethod
    def garden_scores(cls):
        x = 0
        print("Garden scores - ", end="")
        for manager in cls.managers:
            print(manager.name, end="")
            print(": ", end="")
            print(manager.score, end="")
            if x < len(cls.managers) - 1:
                print(", ", end="")
                x += 1
        print("")

    @classmethod
    def total_garden_managed(cls):
        print("Total garden managed:", len(cls.managers))

    @staticmethod
    def test_validation():
        if (GardenManager.height_validation < 0):
            print("Height validation test: False")
        else:
            print("Height validation test: True")


class Plant:
    def __init__(self, name, type, height):
        self.name = name
        self.type = type
        self.height = height

    def grow(self, gr):
        self.height += gr
        if (self.type == "Tree"):
            print(self.name, " ", self.type, " grew ", gr, "cm", sep="")
        else:
            print(self.name, " grew ", gr, "cm", sep="")


class Tree(Plant):
    def __init__(self, name, type, height):
        super().__init__(name, type, height)


class Flower(Plant):
    def __init__(self, name, type, height):
        super().__init__(name, type, height)


class FloweringPlant(Flower):
    def __init__(self, name, type, height, color, flowering):
        super().__init__(name, type, height)
        self.color = color
        self.flowering = flowering


class PrizeFlower(FloweringPlant):
    def __init__(self, name, type, height, color, flowering, prize):
        super().__init__(name, type, height, color, flowering)
        self.prize = prize


if __name__ == '__main__':

    print("=== Garden Management System Demo ===")
    print("")
# create a Garden manager
    alice = GardenManager("Alice")

# create a plants
    oak = Tree("Oak", "Tree", 100)
    rose = FloweringPlant("Rose", "FloweringPlant", 25, "red", 1)
    sunflower = PrizeFlower("Sunflower", "PrizeFlower", 50, "yellow", 1, 10)

# add plants to alice garden!
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print("")
    alice.watering()
    print("=== Alices's Garden Report ===")
    alice.garden_report()
    bob = GardenManager("Bob")
    bob.score = 92
# tmp_manager = GardenManager("tmp")
    GardenManager.test_validation()

# manager = GardenManager("manager")
    GardenManager.garden_scores()
    GardenManager.total_garden_managed()
