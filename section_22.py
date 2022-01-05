# Static Methods

# class Sum:
#     @staticmethod
#     def get_sum(*args):
#         sum_1 = 0
#         for i in args:
#             sum_1 += i
#         return sum_1


# def main():
#     print("Sum :", Sum.get_sum(1,2,3,4,5))

# class Dog:
#     num_of_dogs = 0

#     def __init__(self, name = "Unknown"):
#         self.name = name
#         Dog.num_of_dogs += 1

#     @staticmethod
#     def get_num_of_dogs():
#         print("There are currently {} dogs".format(Dog.num_of_dogs))

# def main():
#     spot = Dog("Spot")
#     doug = Dog("Doug")
#     spot.get_num_of_dogs()

# main()

#Custom modules

#import sum

from sum import get_sum

print("Sum :", get_sum(1,2,3,4,5))