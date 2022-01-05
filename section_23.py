# try:
#     a_list = [1,2,3]
#     print(a_list[3])

# except IndexError:
#     print("Sorry that index exist")

# except:
#     print("An unknown error occurred")


# class DogNameError(Exception):
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)

# try: 
#     dog_name = input("What is your dogs name: ")
#     if any (char.isdigit() for char in dog_name):
#         raise DogNameError
    
# except DogNameError:
#     print("Your dogs name can't contain a number")
        
# num1, num2 = input("Enter two values to divide:").split()

# try: 
#     quotient = int(num1) / int(num2)
#     print("{} / {} = {}".format(num1, num2, quotient))

# except ZeroDivisionError:
#     print("You can't divide by zero")

# else: 
#     print("You didn't raise an exception")

# finally:
#     print("I execute no matter what")

try:
    my_file = open("mydata2.txt", encoding= "utf-8", )

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else: 
    print("File: ", my_file.read())
    my_file.close()
    
finally:
    print("Finished Working with File")
