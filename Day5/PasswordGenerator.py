import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

final_password = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

randomizer = []

for i in range(nr_letters + nr_numbers + nr_symbols):
    randomizer.append(random.randint(0,2))

for i in range(len(randomizer)):
    if(randomizer[i] == 0):
        final_password += letters[random.randint(0, len(letters) - 1)]
    elif(randomizer[i] == 1):
        final_password += numbers[random.randint(0, len(numbers) - 1)]
    elif(randomizer[i] == 2):
        final_password += symbols[random.randint(0, len(symbols) - 1)]

print("Your password is: ")

print(final_password)