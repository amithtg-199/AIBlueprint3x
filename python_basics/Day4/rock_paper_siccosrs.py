import random
actions = ["rock","paper","sissors"]
print("Welcome to the Game of Rock Paper and Sisssors")
user_choice = actions[int(input("What is your choice? type 0 for Rock, 1 for paper and 2 for sissors: "))]
computer_choice = random.choice(actions)
print(f"You selected {user_choice}")
print(f"Computer selected {computer_choice}")

if user_choice == "rock" or user_choice == "paper" or user_choice == "sissors":
    if user_choice == "sissors" and computer_choice == "rock":
        print("you Loose")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You Loose")
    elif user_choice == "paper" and computer_choice == "sissors":
        print("You Loose")
    elif user_choice == computer_choice:
        print("Its a Draw")
    else:
        print("You Win!!!")
else:
    print("You entered wrong choice, kindly enter any one of these choices 0, 1 or 2")
exit(0)