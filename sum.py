# def get_sum(*args):
#     sum_1 = 0
#     for i in args:
#         sum_1 += i
#     return sum_1

# print(10 / 3)
# print(10 // 3)

# x = 10
# x -= 3
# print(x)

# x = 3 > 2
# print(x)

# a single = is assignment
# double equal, i.e  ==, is equality operators

import re


temperature = 5

# if temperature > 30:
#     print("It's a 'hot day'")
#     print("Drink plenty of water")
# elif temperature > 20: #the temperature is (20,30]
#     print("It's a nice day")
# elif temperature > 10:
#     print("It is a bit cold")
# else:
#     print("It's cold")

# weight = int(input("Weight: "))
# unit = str(input("(K)g or (L)bs: "))
# if unit.upper() == "L": #let python know that 
#     converted = weight * 0.453592
#     print("Weight in Kg: " +  str(converted))
# else:
#     converted = weight / 0.45
#     print("Weight in Lbs:" + str(converted))

# i = 1

# while i < 5:
#     print(i)
#     i = i + 1

# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1

# names = ["John", "Bob", "Mosh", "Sam"]
# names[0] = "Jon"
# print(names[0:3])

# numbers = [1,2,3,4,5]
# numbers.insert(0, -1)
# print(numbers)

# for item in numbers:
#     print (item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# numbers = range(5, 10, 2)
# for num in numbers:
#     print(num)

# numbers = (1,2,3)

def fizz_buzz(int):
    if int % 3 == 0:
        print("Fizz")
    elif int % 5 == 0:
        print("Buzz")
    elif  int % 3 ==0 & int % 5 == 0:
        print("FizzBuzz")
    else:
        return(int)

fizz_buzz(30)


def speed_check(spd):
    demerit = 0
    if spd < 70:
        print("Ok")
    elif spd == 75 & spd % 5 == 0:
        demerit += (spd-70)/5
        print("Demerit points :" +str(d))
    if demerit > 12:
        print("Licence suspended")
