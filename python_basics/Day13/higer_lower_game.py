import art
import random
import os
import game_data

def account(data):
    account_name = data["name"]
    account_description = data["description"]
    account_country = data["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

print(art.logo)
a_data=random.choice(game_data.data)

new_game = True
wins=0

while new_game is True:
    if wins > 0:
        print(f"You're right! Current score: {wins}")

    print(f"Compare A: {account(a_data)}")
    print(art.vs)

    b_data=random.choice(game_data.data)

    while a_data == b_data:
        b_data=random.choice(game_data.data)
    print(f"Against B: {account(b_data)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    while user_guess not in ['a', 'b']:
        user_guess = input("kindly input either 'A' or 'B': ").strip().lower()

    a_followers=a_data["follower_count"]
    b_follwers=b_data["follower_count"]

    is_correct = False
    if user_guess == "a" and a_followers >= b_follwers:
        is_correct = True
    elif user_guess == "b" and b_follwers >= a_followers:
        is_correct = True
    
    os.system('cls')
    print(art.logo)

    if is_correct:
        wins += 1
        a_data = b_data
    else:
        print(f"Sorry, that's wrong. Final score: {wins}")
        new_game = False
