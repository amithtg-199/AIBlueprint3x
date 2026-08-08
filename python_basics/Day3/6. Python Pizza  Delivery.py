print("Welcome to Python Pizza")
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni onyour pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You entered wrong input kindly retry again ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print (f"You final bill is ${bill}")
