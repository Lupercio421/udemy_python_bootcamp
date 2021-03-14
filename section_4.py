#name = input("What is your name : ")
#print("Hello", name)

'''
num_1, num_2 = input("Enter 2 Numbers: ").split()

num_1 = int(num_1)
num_2 = int(num_2)

sum_1 = num_1 + num_2
difference = num_1-num_2
product = num_1*num_2
quotient = num_1/num_2
remainder = num_1 % num_2

print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, difference))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))

'''
#Asks the user to input the number of miles

# Convert the miles to kilometers (kilometers = miles * 1.60934)

# Then print this for example 5 miles equals 8.0467 kilometers

'''
miles = int(input("Enter a number: "))

kilometers = miles * 8.0467

print(miles, "miles equals", kilometers, "kilometers")

'''

import math

print("ceil(4.4) = ", math.ceil(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))
