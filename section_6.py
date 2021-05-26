#for i in range(5):
#    print("i =", i )

#i = 6

#print("Is 6 Even :", ((i % 2)==0))

#for i in range(1,21):
#    if (i%2 != 0):
#        print("i =",i)

#your_float = input("Enter a float : ")
#your_float = float(your_float)

#print("Rounded to 2 Decimals : {:.2f}".format(your_float))

#My program will:

#1. Have the user enter their investment amount and expected interest
original_investment = float(input("Enter an investment amount : "))
expected_interest = float(input("What is your expected interest : ")) * .01
#expected_interest = expected_interest * .01

#2. Each year their investment will increase by their investment + their investment * their interest rate
for i in range(10):
    original_investment = original_investment + (original_investment * expected_interest)

#. Print out their earnings after a 10 year period
print("Investment after 10 years : ${:.2f}".format(original_investment))