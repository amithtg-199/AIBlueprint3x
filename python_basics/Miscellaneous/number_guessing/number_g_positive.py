import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
num_guess = random.randint(1, 100)

def guess_game(level):
    num_lives = 10 if level == "easy" else 5

    continue_guess = True
    while num_lives > 0 and continue_guess is True:
        print(f"You have {num_lives} attempts remaining to guess the number")
        user_input = input("Make a guess: ")
        
        # 1. Safely parse string to integer using try-except
        try:
            guess = int(user_input)
        except ValueError:
            print("You entered a non-integer value, you lose a life")
            num_lives -= 1
            print()
            continue

        # 2. Check if the guess is within the range [1, 100] (covers negative values, 0, and numbers > 100)
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds! Choose a number between 1 and 100. You lose a life.")
            num_lives -= 1
            print()
            continue

        # 3. Check the guess value
        if guess == num_guess:
            print(f"You Win!! guessed correct number {guess}")
            continue_guess = False
        elif guess < num_guess:
            print("Too Low \n Guess Again!")
            num_lives -= 1
        elif guess > num_guess:
            print("Too High \n Guess Again!")
            num_lives -= 1
        print()

    if num_lives == 0:
        print("You've run out of guesses. Refresh the page to run again")
        exit()

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while game_level not in ['easy', 'hard']:
    game_level = input("kindly input only 'easy' or 'hard': ").lower()

guess_game(game_level)
