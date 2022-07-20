import art
import os
print(art.logo)
still_on = True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
name_bid = []
def bid_info(bidder, price):
    compiled = {}
    compiled["name"] = bidder
    compiled["bid_price"] = price
    name_bid.append(compiled)
    print(name_bid)

def high_bidders(bidded, payout):
    high_bidders = {}
    for n in name_bid:
        high_bidders[n["name"]] = n["bid_price"]
        for bids in high_bidders:
            highest_price =max(high_bidders, key=high_bidders.get)
    print(f'the highest bidder is {highest_price}')


while still_on:
    name = input("What is your name?:\n")
    bid_price = input("What's your price? :\n")
    bid_info(name, bid_price)
    stop_bid = input("Any player left? type yes or no.\n").lower()
    if stop_bid == "no":
        still_on = False
        high_bidders(name,bid_price)
    else:
        clear_screen()


















