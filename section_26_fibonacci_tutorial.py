'''
Create a class that returns values from the Fibonacci sequence
each time next is called.
Sample Output
Fib : 1
Fib : 2
Fib : 3
Fib : 5
'''
# Fibonacci is the sum of the two previous terms
# starting with 0 + 1
class Fib:
    def __init__(self):
        #Set the first iteration as 0 + 1
        self.x = 0
        self.y = 1
    def __iter__(self):
        # will always return the current iteration
        return self
    def __next__(self):
        # the new value that is returned is the addition
        # of the two terms
        self.new = self.x + self.y
        # Need to set the terms to add up to be the current
        # value (self.new) and the value before it (self.y)
        # In this case the self.new will be assigned to self.x
        # to carry the value for the current term over.
        # The self.x which is the previous self.new gets
        # assigned to self.y so when they are added
        # again, it will be adding up current + previous
        # on every iteration.
        # You have to set the self.y to self.x before you
        # set the self.x to self.new, otherwise it will
        # be doing self.new + self.new on the next iteration
        self.y = self.x
        self.x = self.new
        # returns the new value
        return self.new
# have to define a variable to the class name
# AKA create an object
fib = Fib()
# loops through the first 15 values of the Fibonacci
for i in range(15):
    # using next to loop through the fib object values
    print("Fib :", next(fib))
