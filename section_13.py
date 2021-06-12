# rand_list = ["string", 1.333, 28]
# one_to_ten = list(range(11))

# rand_list = rand_list + one_to_ten
# print(rand_list[0])

# print("List length", len(rand_list))

# first_3 = rand_list[0:3]

# for i in first_3:
#     print("{} : {}".format(first_3.index(i),i))


# print(first_3[0]*3)

# print("Index of string:", first_3.index("string"))
# print("How many strings: ", first_3.count("string"))

# first_3[0] = "New String"

# first_3.append("Another")

# for i in first_3:
#     print("{} : {}".format(first_3.index(i),i))

import random

# num_list = []

# for i in range(5):
#     num_list.append(random.randrange(1,9))

# for i in num_list:
#     print(i)

# BUBBLE SORT
# num_list = []
# for i in range(5):
#     num_list.append(random.randrange(1,9))

# for i in num_list:
#     print(i, end="")

# i = len(num_list) - 1
# while i > 1:
#     j = 0
#     while j < i:
#         print("\nIs {} > {}".format(num_list[j],num_list[j+1]))
#         print()
#         if num_list[j] > num_list[j+1]:
#             print("Switch")
#             temp = num_list[j]
#             num_list[j] = num_list[j+1]
#             num_list[j+1] = temp
#         else:
#             print("Don't Switch")
#         j += 1
#         for k in num_list:
#             print(k, end="")
#         print()
#     print("End of Round")
#     i -= 1
#     for k in num_list:
#         print(k, end="")
#     print()


# num_list = []
# for i in range(5):
#     num_list.append(random.randrange(1,9))

# (num_list.sort())
# (num_list.reverse())

# num_list.insert(5,10)

# num_list.remove(10)
# num_list.pop(2)

# for k in num_list:
#     print(k, end=", ")

# print()

import random
my_list = [5,2,9,1]

num_list = []
for i in range(5):
    num_list.append(random.randrange(0,5))
    
print("Length: ", len(my_list))

print(my_list[0])

print(my_list[0:3])

print("Is 9 in my_list:", 9 in my_list)

print("Index of 2: ", my_list.index(2))
print("How many 2's: ", my_list.count(2))

my_list.remove(1)
my_list[0] = 10


my_list.sort()
print("Sorted: ", my_list)

my_list.reverse()
print("Sorted: ", my_list)