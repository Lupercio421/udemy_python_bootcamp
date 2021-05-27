import random

#random_num = random.randrange(1,51)
#i = 1
#while i != random_num:
#    i += 1 #i = i+1

#print("The random value is : ", random_num)

#i = 1
#while i <= 40:
#    if (i%2) == 0:
#        i += 1
#        continue #skip back to the beginning of a loop
#   if i == 39:
#        break
#    print("Odd : ", i)
#    i += 1

tree_height = int(input("How tall is the tree : "))

spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print(' ', end = "")
    for i in range(hashes):
        print('#', end = "")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
    print(" ", end = "")
print("#")