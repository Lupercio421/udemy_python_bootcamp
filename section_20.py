class Animal:
    def __init__(self, birth_type = "Unknown", appearence = "Unkown", blooded = "Unknown"):
        self.__birth_type = birth_type
        self.__appearence = appearence
        self.__blooded = blooded


    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    @property
    def appearence(self):
        return self.__appearence

    @appearence.setter
    def appearence(self, appearence):
        self.__appearence = appearence
    
    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded
    
    def __str__(self):
        return "A {} is {} it has {} it is {}".format(type(self).__name__, self.birth_type, self.appearence, self.blooded)

class Mammal(Animal):
    def __init__(self, birth_type = "born alive", appearence = "hair or fur", blooded = "warm blooded", nurse_young = True):
        Animal.__init__(self, birth_type, appearence, blooded)
        self.__nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young
    
    def __str__(self):
        return super().__str__() + "and it has {} they nurse their young".format(self.nurse_young)

class Reptile(Animal):
    def __init__(self, birth_type = "born in an egg or born alive", appearence = "dry_scales", blooded = "cold_blooded"):
        Animal.__init__(self, birth_type, appearence, blooded)

def main():
    animal1 = Animal("born alive")
    print(animal1.birth_type)
    print(animal1)

    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.birth_type)
    print(mammal1.appearence)
    print(mammal1.blooded)
    print(mammal1.nurse_young)

    reptile1 = Reptile()
    print(reptile1)
    print(reptile1.birth_type)
    print(reptile1.appearence)
    print(reptile1.blooded)
    

main()