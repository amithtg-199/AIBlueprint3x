import art
import os

print(art.logo)

bid_continue = True
bid_entry = {}

while bid_continue:
    name = input("What is your name?: ")
    amount = int(input("What is your bid $"))
    bid_entry[name] = amount

    any_other_bidder = input("Are there any other bidders? Type 'yes or 'no'.")
    if any_other_bidder == "no":
        bid_continue = False
    else:
        os.system('cls')
    
highest_bidder_name = max(bid_entry, key=bid_entry.get)
highest_bid_amount = max(bid_entry.values())
print(f"The Winner is {highest_bidder_name} with bid of ${highest_bid_amount}")