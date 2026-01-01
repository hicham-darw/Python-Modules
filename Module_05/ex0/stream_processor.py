from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("im animal class!")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class Wolf(Animal):
    def make_sound(self):
        print("Whooo!")


wolf = Wolf()
cat = Cat()
print("this wolf:")
wolf.make_sound()
print("this cat:")
cat.make_sound()

