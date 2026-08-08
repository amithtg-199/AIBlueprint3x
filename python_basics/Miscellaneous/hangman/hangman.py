import hangman_art
import hangman_words
import random

print (hangman_art.logo)

word_to_guess = random.choice(hangman_words.word_list)
blank_spaces=[]

for word in range(0, len(word_to_guess)):
    blank_spaces.append("_")

num_lives=6

while num_lives >0:
    print(f"Word to guess: {''.join(blank_spaces)}")
    guess=input(f"Guess a letter: ").lower()
    for i in range(0,len(blank_spaces)):
        if guess == word_to_guess[i]:
            blank_spaces[i]=guess
    if guess not in word_to_guess:
        print(f"You guessed {guess}, that's not in word, You lose a life")
        num_lives -= 1
    print(''.join(blank_spaces))
    print(hangman_art.stages[num_lives])
    print(f"***********************************{num_lives}/6********************************")
    if ''.join(blank_spaces) == word_to_guess:
        print(f"You Won!!")
        break

print(f"***********************IT WAS {word_to_guess}! YOU LOSE**********************")