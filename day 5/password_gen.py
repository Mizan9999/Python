import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator")
password = []
letters_length = int(input("How many letters you want?\n"))
numbers_length = int(input("How many numbers you want?\n"))
symbols_length = int(input("How many symbols you want?\n"))

for char in range(0, letters_length):
    password.append(random.choice(letters))
for char in range(0, numbers_length):
    password += random.choice(numbers)
for char in range(0, symbols_length):
    password += random.choice(symbols)

random.shuffle(password)

final = ""
for char in password:
    final += char

print(final)