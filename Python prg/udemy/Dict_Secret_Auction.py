print("Welcome to the Secret Auction Program !")
def max_bidder(bidding_dict):
    winner_name=""
    highest_bid=0
    for i in bidding_dict:
        if(bidding_dict[i]>highest_bid):
            highest_bid=bidding_dict[i]
            winner_name=i
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")


bid={}
while(True):
    name=input("Enter your name: ")
    amount=int(input("Enter your bid amount: "))
    bid[name]=amount
    choice=input("Are there any other bidders (y or n)")
    if(choice=="y"):
        print("\n"*20)
        continue
    elif(choice=="n"):
        max_bidder(bid)
        break