'''
Generate a List of Odds
To solve this problem:
1. Create a function is_it_odd that will receive a number and return True if it is odd
and False otherwise
2. Create a list of values from 1 to 20
3. Create a function named change_list that received a list and the function is_it_odd
4. change_list will use the function is_it_odd on each value in the list and return a
new list of just those odd values
5. Sample Output :
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
'''
# 1. Create a function is_it_odd that will receive a number and return True if it is odd
# and False otherwise
def is_it_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

# 2. Create a list of values from 1 to 20
num_list = list(range(1,21))

# 3. Create a function named change_list that received a list and the function is_it_odd
# 4. change_list will use the function is_it_odd on each value in the list and return a
# new list of just those odd values
def change_list (list, is_it_odd):
    odd_list = []
    for i in list:
        if is_it_odd(i):
            odd_list.append(i)
    print(odd_list)

# main function to run change_list
def main():
    change_list(num_list, is_it_odd)
main()
