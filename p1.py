from replit import clear
print("                     " )
print("───█▒▒░░░░░░░░░▒▒█───")
print("────█░░█░░░░░█░░█────")
print("─▄▄──█░░░▀█▀░░░█──▄▄─")
print("█░░█─▀▄░░░░░░░▄▀─█░░█")
print("--------Lets start the bid:-------")
bids ={}
bidding_fineshed=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount =bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print("The winner is"+str(winner)+"with the highest bid of $"+str(highest_bid))

while not bidding_fineshed:
    name=input("What is your name")
    price =int(input("What is your bid ? $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes'or'no'.")
    if should_continue=="no":
       bidding_fineshed=True
       find_highest_bidder(bids)
    elif should_continue =="yes":
       clear()