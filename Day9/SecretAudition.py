logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidder_dic = {}

def addBidderWithInput():
    key = input("What's the name of the bidder ? \n")
    value = float(input("Whats is the value of the bid ? \n$"))
    bidder_dic[key] = value

def compareBidders():
    global bidder_dic
    highest_bid_key = ""
    highest_bid = 0.0
    for key in bidder_dic:
        if(bidder_dic[key] > highest_bid):
            highest_bid_key = key
    return highest_bid_key

def makeSecretAudiction():
    print(logo+ "\n")
    resp = ""
    while(resp != "no"):
        addBidderWithInput()
        resp = input("Are there any other bidder ? Type 'yes' or 'no'\n")
    key = compareBidders()
    print("the winner is " + key +" with a bid of $" + str(bidder_dic[key]))

makeSecretAudiction()