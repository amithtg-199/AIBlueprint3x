print("Welcome to RollerCoaster Ride!")
height_cm = int(input("Enter your height in cms: "))
if height_cm >= 120:
    age = int(input("Enter your Age: "))
    if age <= 18:
        print("You are eligible for the ride kindly pay $7 at the counter")
    else:
        print("You are eligible for the ride kindly pay $12 at the counter")
else:
    print("Sorry your height below 120cms, you are not eligible for the ride")