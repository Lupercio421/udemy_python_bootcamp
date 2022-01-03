import os

# with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
#     my_file.write("Some random text \nMore random text\nAnd more")

# with open("mydata.txt", encoding="utf-8") as my_file:
#     print(my_file.read())

# print(my_file.closed)

# print(my_file.name)
# print(my_file.mode)
# os.rename("mydata.txt", "mydata2.txt")
# # os.remove("mydata2.txt")
# # os.mkdir("mydir")
# # os.chdir("mydir")
# # print("Current Directory : ", os.getcwd())


# with open("mydata2.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print("Line : ", line_num, " : ", line,end = "")
#         line_num += 1

# Python Problem for you to Solve

# For this problem I want you to cycle through each line of text and output the number of words and the average word length
# Here is sample output.

# Line 1
# Number of Words : 3
# Avg Word Length : 4.7
# Line 2
# Number of Words : 3
# Avg Word Length : 4.7

# import os

# with open("mydata2.txt", encoding="utf-8") as my_file:
#     line_num = 1

#     while True:
#         line = my_file.readline()

#         # line is empty so exit
#         if not line:
#             break

#         print("Line", line_num)

#         # Put the words in a list using the space as the boundary between words
#         word_list = line.split()

#         # Get the number of words with len()
#         print("Number of Words :", len(word_list))

#         # Incremented for each character
#         char_count = 0

#         for word in word_list:
#             for char in word:
#                 char_count += 1

#         # Divide to find the answer
#         avg_num_chars = char_count/len(word_list)

#         # Use format to limit to 2 decimals
#         print("Avg Word Length : {:.2}".format(avg_num_chars))

#         lineNum += 1

my_tuple = (1,2,3,5,8)

print("1st Value:", my_tuple[0])

print(my_tuple[0:3])

print("Length : ", len(my_tuple))

more_fibs = my_tuple + (13, 231, 34)

print("34 in Tuple :", 34 in more_fibs)

for i in more_fibs:
    print(i)

a_list = [55, 89, 144]

a_tuple = tuple(a_list)

a_list = list(a_tuple)

print("Max : ", max(a_tuple))
print("Min : ", min(a_tuple))