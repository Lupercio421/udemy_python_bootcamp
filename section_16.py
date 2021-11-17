# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         result = num * factorial(num-1)
#         return result
# print(factorial(4))

# 1,1,2,3,5,8,...

# The Fibo. sequence is define by: 
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

# def fibo(n):
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         result = fibo(n - 1) + fibo(n-2)
#         return result

# print(fibo(2))
# print(fibo(3))



def fibo(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else: 
        result = fibo(n - 1) + fibo(n-2)
        return result

num_fib_vals = int(input("How many Fibonacci values should be found?: "))

i = 1
while i < num_fib_vals:
    fib_value = fibo(i)
    print(fib_value)
    i += 1