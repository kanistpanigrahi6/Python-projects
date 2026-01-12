def highest_bidder(bidding_dict):
    winner=""
    highest_bid=0
    max(bidding_dict)
    for bidder in bidding_dict:
        bid_amount=bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner}with a bid of  {highest_bid}")


bids={}
continue_bidding=True
while continue_bidding:
    name=input("Whats ur name:")
    price=int(input("Bid price..?:"))
    bids[name]=price
    others=input("Type YES if there are other users to bid other wise type NO").lower()
    if others=="no":
        continue_bidding = False
        highest_bidder(bids)
    elif   others=="yes":
        print("\n"*30)






