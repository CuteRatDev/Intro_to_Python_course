# TODO-1: Ask the user for input

# TODO-2: Save the data into dictionary {name:price}

# TODO-3: Wheather if new bids need ot be added

auction_finished = False
auction = {


}

def start_auction():
    auc_name = input("What is your name? \n")
    auc_bid = float(input("What is your bid? \n"))
    auction.update({auc_name: auc_bid})

while not auction_finished:
    start_auction()
    print("\n" * 100)
    auction_finished = input("Do you want to continue? (y/n)").lower()
    if auction_finished == "y":
        auction_finished = False
    else:
        auction_finished = True

winning_bid = max(auction,key=auction.get)
winning_value = auction[winning_bid]

print(f"The winner is {winning_bid} with a bid of ${winning_value}")