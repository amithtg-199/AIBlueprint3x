import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd=[]
""" get letter from list based on value of nr_letters"""
for letter in range (0, nr_letters):
    pwd.append(random.choice(letters))

for symbol in range (0, nr_symbols):
    pwd.append(random.choice(symbols))

for number in range(0, nr_numbers):
    pwd.append(random.choice(numbers))
random.shuffle(pwd)
final_password = ''.join(pwd)

print(f"Hi! your Password is : {final_password}")


    