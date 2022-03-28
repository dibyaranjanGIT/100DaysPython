from replit import clear
import art

# Displaying the logo
print(art.logo)

bidding_details = {}
user_available = True

def find_heighest_bidder(bidding_details):
    heighest_bid = 0
    winner = ''
    for name, amount in bidding_details.items():
        if amount > heighest_bid:
            heighest_bid = amount
            winner = name

    print(f"The heigest bidder is {winner} with bidding amount ${heighest_bid}")

while user_available:
    # Asking for user inputs
    user_name = input("Enter your name : ")
    bidding_amount = int(input("Enter your bidding amount$ : "))

    bidding_details[user_name] = bidding_amount

    end_game = input("Do we have anyone left ? yes or no : ")
    if end_game == "no":
        find_heighest_bidder(bidding_details)
        user_available = False

    clear()




