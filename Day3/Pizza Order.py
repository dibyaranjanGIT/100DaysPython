print("Welcome !!")
Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25
bill = 0

size = input("What size do you want? S, M or L")
extra_cheese = input("Do you want extra cheese ? Y or N")

if size == "S" and extra_cheese == 'Y':
    bill = Small_Pizza + 2
else:
    bill = Small_Pizza

if size == "M" and extra_cheese == 'Y':
    bill = Medium_Pizza + 3
else:
    bill = Medium_Pizza

if size == "L" and extra_cheese == 'Y':
    bill = Large_Pizza + 1
else:
    bill = Large_Pizza
