# def add_numbers(num_1, num_2):
#     return num_1+num_2
# print("5 + 4 = ", add_numbers(4, 5))

# def change_name():
#     global globalname
#     globalname = "Sammy"



# globalname = 'Sally'
# change_name()
# print(globalname)

# The try statement catches expressions. try statements can specify except clauses
# with suites that serve as handlers for exceptions raised during the try suite;

# def is_float(str_val):
#     try:
#         float(str_val)
#         return True
#     except ValueError:
#         return False

# pi = "A"
# print("Is Pi a Float: ", is_float(pi))


# def solve_eq(equation):
#     x, add, num_1, equal, num_2 = equation.split() #split returns a list of the words in the string 'equation'
    #using sep as the delimiter string
#     num_1, num_2 = int(num_1), int(num_2)
#     return "x = " + str(num_2 - num_1)

# print(solve_eq("x + 4 = 9"))


def is_str(str_val):
    try:
        str(str_val)
        return True
    except ValueError:
        return False

string = 'Danny'
print("Is Danny a String ", is_str(string))
string2 = 21
print("Is 21 a String ", is_str(string2))
print(str(21)) # This was going to work anyway, as str(21) will return 21 as a string
print(list("Danny"))