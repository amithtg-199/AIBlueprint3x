import random
import art
import os


def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list as input and return the sum as the output"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """This function compares the user and computer scores and returns the matching results"""
    if computer_score == user_score:
        return "Its a Draw"
    elif computer_score == 0:
        return "Your Opponent has BlackJack, You Lose"
    elif user_score == 0:
        return "You have a blackjack, You Win"
    elif user_score > 21:
        return "You crossed 21 mark, You Lose"
    elif computer_score > 21:
        return "You opponent went over 21, You Win"
    elif user_score > computer_score:
        return "Your total is more than opponents score, you win"
    else:
        return "You Lose"


def blackjack():
    user_cards = []
    computer_cards = []
    user_card_sum = -1
    computer_card_sum = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_card_sum = calculate_score(user_cards)
        computer_card_sum = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}, and your sum is: {user_card_sum}")
        print(f"Computers first card is: {computer_cards[0]}")
        if user_cards == 0 or computer_cards == 0 or user_card_sum > 21:
            is_game_over = True
        else:
            game_cont_input = input("Do you want to choose another card type 'y' for yes and 'n' for no: ").lower()
            if game_cont_input == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_card_sum != 0 and computer_card_sum < 17:
        computer_cards.append(deal_card())
        computer_card_sum = calculate_score(computer_cards)

    print(f"Your final Score is: {user_card_sum}")
    print(f"Your Opponents final score is: {computer_card_sum}")
    print(compare(user_card_sum, computer_card_sum))


while input("Do you want to play the game of blackjack, type 'y' for yes and 'n' for no: ").lower() == "y":
    os.system('cls')
    print(art.logo)
    blackjack()














