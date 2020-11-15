from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

bids = {}

# Store bids in a dictionary
def new_bid():
    print(logo)
    print("Welcome to the secret auction program.\n")

    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bids[name] = bid

# Find the highest bidder
def find_high_bid():
    high_bid = 0.0
    high_bidder = ""
    for bidder in bids:
        if bids[bidder] > high_bid:
            high_bid = bids[bidder]
            high_bidder = bidder
    print(f"The winner is {high_bidder} with a bid of ${high_bid:.2f}")

# Get bids
get_bids = True
while get_bids:
    new_bid()
    more_bids = input("Are there any other bidder? Type 'yes' or 'no'. ").lower()
    if more_bids == "no":
        get_bids = False
    clear()
find_high_bid()
