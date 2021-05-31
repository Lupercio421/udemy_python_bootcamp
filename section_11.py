# def add_numbers(num_1, num_2):
#     return num_1+num_2
# print("5 + 4 = ", add_numbers(4, 5))

# def change_name():
#     global globalname
#     globalname = "Sammy"



# globalname = 'Sally'
# change_name()
# print(globalname)

# def is_float(str_val):
#     try:
#         float(str_val)
#         return True
#     except ValueError:
#         return False

# pi = "A"
# print("Is Pi a Float: ", is_float(pi))


def solve_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)
    return "x = " + str(num_2 - num_1)

print(solve_eq("x + 4 = 9"))
