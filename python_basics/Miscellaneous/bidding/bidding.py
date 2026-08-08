import logo
import os

print(logo.logo)
bid_dict = {}

bid_continue = True

while bid_continue is True:
    bidder_name=(input("What is your name?: ").lower())
    while True:
        try:
            bid_amount=(int(input("What is your bid?: $")))
            break
        except ValueError:
            print("Invalid Input. Please enter number only")

    bid_dict[bidder_name] = bid_amount

    is_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while is_continue not in ["yes", "no"]:
        is_continue = input("Kindly input either 'yes' or 'no' only: ").lower()

    if is_continue == "yes":
        os.system('cls')
    else:
        bid_continue = False

max_bid = 0
max_bid_name = []
for name in bid_dict:
    current_bid = bid_dict[name]
    if current_bid > max_bid:
        max_bid = bid_dict[name]
        max_bid_name = [name]
    elif current_bid == max_bid:
        max_bid_name.append(name)

if len(max_bid_name) > 1:
    all_winners = ", ".join(max_bid_name)
    print(f"it's a tie!! and winners are {all_winners} with a bid value of {max_bid}")
else:
    print(f"The winner is {max_bid_name} with a bid of ${max_bid}")




