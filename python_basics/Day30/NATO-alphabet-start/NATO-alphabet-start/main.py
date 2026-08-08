import pandas as pd
#TODO 1. Create a dictionary in this format:
df = pd.read_csv(r"Python_codes_new\Day26\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your word: ").upper().strip()

'''Here split is used because it fetches words from a sentance as items for the list so = 1 means it's a word'''
if len(user_input.split()) == 1:
    phonetic_word = [nato_phonetic_dict[char] for char in user_input]
    print(phonetic_word)

elif len(user_input.split()) == 0:
    print("You have not entered any word, kindly retry")

else:
    print("You entered a sentance instead a word kindly retry")
