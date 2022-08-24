import art
import os

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print(art.logo)

bids = {}
bidding_complete = False


def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, and they won with a bid of ${highest_bid}")


while not bidding_complete:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))

    bids[name] = price

    should_continue = input("Are there any more bidders? Type 'yes' or 'no': ").lower()

    if should_continue == 'no':
        bidding_complete = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear_console()
        print(art.logo)
