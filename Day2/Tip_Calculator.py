print("Welcome to the tip calcualtor!")
bill = float(input("What was the bill amount $ "))
tip = int(input("How much tip you would like to give ? "))

people = int(input("How many people to split the bill ?"))
bill_with_tip = tip / 100 * bill + bill

bill_with_tip = "{:.2f}".format(bill_with_tip)
print(bill_with_tip)