# rand_string = "     this is an important string     "

# rand_string = rand_string.lstrip()
# rand_string = rand_string.strip()

rand_string = "this is an important string"

# print(rand_string.upper())

# a_list = ["Bunch", "of", "random", "words"]

# print("".join(a_list))

# a_list2 = rand_string.split()

# for i in a_list2:
#     print(i)

print("Where is :", rand_string.replace(" an", " a kind of"))

# Convert to Acronym: Random Access Memory "RAM"

# original_string = input("Convert to Acronym: ")
# original_string = original_string.upper()
# list_of_words = original_string.split()
# for word in list_of_words:
#     print(word[0], end="")
# print()

# letter_z = "z"
# print("Is z a letter or number: ", letter_z.isalnum())
# print("Is z a letter or digit: ", letter_z.isdigit())
letter_z.is
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))

secret_message = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26

        secret_message += chr(char_code)
    else:
        secret_message += char 
print("Encrypted: ", secret_message) 

key = -key
orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26 
        
        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decryped: ", orig_message)