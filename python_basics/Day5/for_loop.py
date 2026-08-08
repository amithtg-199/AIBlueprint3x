# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

import random
password = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
for i in range(1,12):
    password.append(random.choice(letters))
#print(password)

for i in range(1,5):
    password.append(random.choice(numbers))
#print(password)

for i in range(1,4):
    password.append(random.choice(symbols))
random.shuffle(password)
passw_str = ''.join(password)
print(passw_str)

