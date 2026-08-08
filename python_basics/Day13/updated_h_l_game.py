import art
import random
import os
import game_data

def format_data(account):
    """Takes the account dictionary and returns a printable format without the follower count."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

print(art.logo)

# Initialize wins OUTSIDE the loop
wins = 0
new_game = True

# Pick the initial A
a_data = random.choice(game_data.data)

while new_game is True:
    if wins > 0:
        print(f"You're right! Current score: {wins}")
        
    # Format and print A
    print(f"Compare A: {format_data(a_data)}")
    print(art.vs)

    # Pick B and ensure it's different from A
    b_data = random.choice(game_data.data)
    while a_data == b_data:
        b_data = random.choice(game_data.data)
        
    # Format and print B (Notice this is outside the while loop now)
    print(f"Against B: {format_data(b_data)}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while user_guess not in ['a', 'b']:
        user_guess = input("Kindly input either 'A' or 'B': ").lower()

    # Get the actual follower counts to compare
    a_follower_count = a_data["follower_count"]
    b_follower_count = b_data["follower_count"]

    # Check if the user is correct
    is_correct = False
    if user_guess == "a" and a_follower_count > b_follower_count:
        is_correct = True
    elif user_guess == "b" and b_follower_count > a_follower_count:
        is_correct = True

    os.system('cls')
    print(art.logo)

    if is_correct:
        wins += 1
        # Sync the data for the next round! B becomes the new A.
        a_data = b_data
    else:
        print(f"Sorry, that's wrong. Final score: {wins}")
        new_game = False
