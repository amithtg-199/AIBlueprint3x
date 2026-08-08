print("Welcome to RollerCoaster Ride!")
height_cm = int(input("Enter your height in cms: "))
bill = 0
if height_cm >= 120:
    print("Hurray! You are eligible for the ride")
    age = int(input("kindly Enter your Age to procced further: "))
    if age < 12:
        bill = 5
        print("child fare is $5")
    elif age >= 12 and age <=18:
        bill = 7
        print("youth fare is $7")
    else:
        bill = 12
        print("Adult fare is $12")
    wants_photo = input("Do you want a photo type y for Yes or n for No ")
    if wants_photo == "y":
        bill += 3
        print(f"kindly pay amount ${bill} at the counter")
    else:
        print(f"kindly pay amount ${bill} at the counter")

else:
    print("Sorry your height below 120cms, you are not eligible for the ride")