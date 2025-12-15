from abc import ABC, abstractmethod

class  Flower:
    @abstractmethod
    def blooming():
        pass

class Rose:
    def blooming ():
        print("blooming now!")

class Gernina:
    def blooming ():
        print("gernina everywher!")

class FactoryPlant:
    def create_plant(self, n):
        if (n == 1):
            return (Rose.blooming())
        elif (n == 2):
            return (Gernina.blooming)
        else:
            return ("t9awed")




gn = Gernina.blooming()
rose = Rose.blooming()
