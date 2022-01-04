from typing import Protocol

# class Dog:
#     def __init__(self, name="", height = 0, weight = 0):
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def run(self):
#         print("{} the dog runs".format(self.name))

#     def eat(self):
#         print("{} the dog eats".format(self.name))
    
#     def bark(self):
#         print("{} the dog barks".format(self.name))

# def main():
#     spot = Dog("Spot", 66, 26)
#     spot.bark()


class Square:
    def __init__(self, height = "0", width = "0"):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        print("Retreiving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")
    @property
    def width(self):
        print("Retreiving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for height")

    def get_area(self):
        return int(self.__width) * int(self.__height)

def main():
    square = Square()
    height = input("Enter Height: ")
    width = input("Enter Width : ")
    square.height = height
    square.width = width
    print("Height : ", square.height)
    print("Width : ", square.width)
    print("The area is :", square.get_area())

main()

