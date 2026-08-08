import pandas as pd

df = pd.read_csv(r"Day30\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}

while True:
    user_input = input("Enter your word: ").upper().strip()
    try:
        '''Here split is used because it fetches words from a sentance as items for the list so = 1 means it's a word'''
        if len(user_input.split()) == 1:
            phonetic_word = [nato_phonetic_dict[char] for char in user_input]
            print(phonetic_word)
        elif len(user_input.split()) == 0:
            raise ValueError("You have not entered any word, kindly retry")
        else:
            raise ValueError("You entered a sentance instead a word kindly retry")
        break
    except KeyError:
        print("Sorry only letters in the alphabet.")
    except ValueError as errmsg:
        print(errmsg)
    except ValueError as err_msg:
        print(err_msg)
        


