import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
num_guess = random.choice(range(1,101))


def guess_game(level):
    num_lives=0
    if level == "easy":
        num_lives=10
    elif level == "hard":
        num_lives=5

    continue_guess=True
    while num_lives >0 and continue_guess is True:
        print(f"You have {num_lives} attempts remaining to guess the number")
        guess = input("Make a guess: ")
        while not guess.isdigit():
            print("You enterd a non-integer value or a negative value, you loose a life")
            num_lives -= 1
        guess = int(guess)
        if guess == num_guess:
            print(f"You Win!! guessed correct number {guess}")
            continue_guess = False
        elif guess < num_guess:
            print("Too Low \n Guess Again!")
            num_lives-=1
        elif guess > num_guess:
            print("Too High \n Guess Again!")
            num_lives-=1
    if num_lives == 0:
        print("You've run out of guesses. Refresh the page to run again")
        exit()

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while game_level not in ['easy','hard']:
    game_level = input("kindly input only 'easy' or 'hard'").lower()

guess_game(game_level)





