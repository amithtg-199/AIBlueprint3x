print("Welcome to RollerCoaster Ride!")
height_cm = int(input("Enter your height in cms: "))
if height_cm >= 120:
    print("Hurray! You are eligible for the ride")
    age = int(input("kindly Enter your Age to procced further: "))
    if age < 12:
        print("kindly pay $5 at the counter")
    elif age >= 12 and age <=18:
        print("Kindly pay $7 at the counter")
    else:
        print("kindly pay $12 at the counter")
else:
    print("Sorry your height below 120cms, you are not eligible for the ride")