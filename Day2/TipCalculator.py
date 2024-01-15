print("Welcome to the Tip Calculator.")
total = float(input("What's the total of the bill? $"))
percentageOfTip = int(input("What porcentage tip would you like to give? 10, 12 or 15 "))/100
quantityOfPayers = int(input("How many people to split the bill? "))

each = (total * (1 + percentageOfTip)) / quantityOfPayers

print("Each person should pay: ", round(each, 2))
