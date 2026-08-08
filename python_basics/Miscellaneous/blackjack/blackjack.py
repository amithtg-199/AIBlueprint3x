import logo
import os
import random



def check_blackjack(user_hand,computer_hand):
    if sum(user_hand) == 21:
        print(f"You win!! Computer score is {sum(computer_hand)} and user's score is {sum(user_hand)}")
        return "win"
    elif sum(computer_hand) == 21:
        print(f"You loose.. Computer score is {sum(computer_hand)} and user's score is {sum(user_hand)}")
        return "loose"
    elif sum(user_hand) == 21 and sum(computer_hand) == 21:
        print(f"Its a draw!! Computer score is {sum(computer_hand)} and user's score is {sum(user_hand)}")
        return "draw"
    elif sum(computer_hand) > 21:
        print(f"It's Bust.. you win!! Computer score is {sum(computer_hand)} and user's score is {sum(user_hand)}")
        return "win"
    elif sum(user_hand) > 21:
        print(f"It's a Bust.. Your Loose.. Computer score is {sum(computer_hand)} and user's score is {sum(user_hand)}")
        return "loose"
    else:
        return "check"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    start_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while start_play not in ['y', 'n']:
        start_play = input("kindly enter only 'y' or 'n'")
    if start_play == 'n':
        print("See you next time!!")
        exit()
    else:
        os.system('cls')
        print(logo.logo)
        user_cards = random.choices(cards, k=2)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        computer_cards = random.choices(cards, k=2)
        print(f"Computer's first card: {computer_cards[0]}")
        restart_blackjack = False
        while restart_blackjack is False:
            if check_blackjack(user_hand=user_cards, computer_hand=computer_cards) in ["win", "loose", "draw"]:
                restart_blackjack = True
                blackjack()
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass:")
                while another_card not in ['y', 'n']:
                    another_card = input("kindly enter only 'y' or 'n'")
                if another_card == "y":
                    new_user_card = random.choice(cards)
                    if new_user_card == 11 and sum(user_cards)+11 > 21:
                        user_cards.append(1)
                    else:
                        user_cards.append(new_user_card)
                    
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's first card: {computer_cards[0]}")

                    if check_blackjack(user_hand=user_cards, computer_hand=computer_cards) in ["win", "loose", "draw"]:
                        restart_blackjack = True
                        blackjack()
                else:
                    while sum(computer_cards) < 17:
                        new_computer_card = random.choice(cards)
                        if new_computer_card == 11 and sum(computer_cards) + 11 > 21:
                            computer_cards.append(1)
                        else:
                            computer_cards.append(new_computer_card)

                    if check_blackjack(user_hand=user_cards, computer_hand=computer_cards) in ["win", "loose", "draw"]:
                        restart_blackjack = True
                        blackjack()
                    else:
                        if sum(user_cards) < sum(computer_cards):
                            print(f"You loose.. Computer score is {sum(computer_cards)} and user's score is {sum(user_cards)}")
                            restart_blackjack = True
                            blackjack()
                        elif sum(user_cards) > sum(computer_cards):
                            print(f"You win.. Computer score is {sum(computer_cards)} and user's score is {sum(user_cards)}")
                            restart_blackjack = True
                            blackjack()
                        else:
                            print(f"It's a draw! Both have {sum(user_cards)}")
                            restart_blackjack = True
                            blackjack()
                        
blackjack()