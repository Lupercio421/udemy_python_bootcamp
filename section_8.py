#while True:
#    try:
#        number = int(input("Please enter a number : "))
#        break

#    except ValueError:
#        print("You did not enter a number")
#    except:
#        print("An unkown error occurred")

#print("Thank you for entering a number")

# do {}

# My attempt
#number = 7
#while True:
#    try:
#        guess = int(input("Guess a number between 1 and 10 : "))
#        while number != guess:
#            print("That wasn't quite it, try again")

#number = 7
#while True:
#    guess = int(input("Guess a number between 1 and 10 : "))
#    if guess == number: 
#        print("You guessed it")
#        break

#rom decimal import Decimal as D

#sum = D(0)
#sum += D("0.01")
#sum += D("0.01")
#sum += D("0.01")
#sum -= D("0.03")
#print("Sum = ", sum)

from decimal import *

sum_1 = Decimal(0)
sum_1 += Decimal("0.011111111111111")
sum_1 += Decimal("0.011111111111111")
print("Sum =", sum_1)
sum_1 -= Decimal("0.022222222222222")
print("Sum =", sum_1)