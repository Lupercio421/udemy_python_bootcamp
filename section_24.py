# def mult_by_2(num):
#     return num*2

# time_two = mult_by_2
# print("4 * 2 = ", time_two(4))

# def do_math(func, num):
#     return func(num)

# print("8 * 2 = ", do_math(mult_by_2, 8))

# def get_func_mult_by_num(num):
#     def mult_by(value):
#         return num * value

#     return mult_by

# generated_func = get_func_mult_by_num(5)

# print("5 * 9 =", generated_func(9))

# list_of_funcs = [time_two, generated_func]

# print("5 * 9 =", list_of_funcs[1](9))

# def is_it_odd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True

# def change_list(list, func):
#     odd_list = []

#     for i in list:
#         if func(i):
#             odd_list.append(i)

#     return odd_list

# a_list = range(1,20)

# print(change_list(a_list, is_it_odd))

def random_func (name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age :", age)
    print("Weight :", weight)
    return "{} is {} years old and weighs {}". format(name, age, weight)

print(random_func(89, "Derek", "Turtle"))

print(random_func.__annotations__)