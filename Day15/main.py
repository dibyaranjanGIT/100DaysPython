from art import logo

from replit import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(logo)

# Turn off the Coffee Machine by entering “off” to the prompt
switch_off = 'off'


# Print report
def report(resources):
    for resource, quantity in resources.items():
        print(f"{resource} : {quantity}")


# Make Coffee
def make_coffee(user_input):
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]


# Process coins
def process_coin(u_money, coffee_cost):
    """Return true of the user has enough money"""
    if u_money >= coffee_cost:
        u_money -= coffee_cost
        return True
    else:
        return False


# Check resources sufficient?
def check_resource(us_choice, resource, us_money):
    """Return True if the resources are enough and user paid enough to make the coffee else return False"""
    if resource["water"] >= MENU[us_choice]["ingredients"]["water"] \
            and resource["coffee"] >= MENU[us_choice]["ingredients"]["coffee"]:
        make_coffee(us_choice)
        if process_coin(us_money, MENU[us_choice]["cost"]):
            return True
        else:
            print("You don't have enough money !")
            return False
    else:
        print("Sorry, we don't have enough resource !")
        return False


# Check transaction successful?
machine_on = True


def is_transaction_success(choice, resource, money):
    """Return True if the transaction is successful"""
    global profit
    if check_resource(choice, resource, money):
        print(f"Your coffee {choice} ☕ is ready for you !")
        report(resource)
        profit += MENU[choice]['cost']
        return True
    else:
        return False


# Asking user to put the amount
turn_on = True
while turn_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    change = 0
    user_choice = input("What would you like? \nType 'espresso' or Type 'latte' "
                        "or Type 'cappuccino' : ").lower()
    money_received = float(input("Enter the money you are paying for your coffee $"))
    if is_transaction_success(user_choice, resources, money_received):
        change = money_received - MENU[user_choice]["cost"]
        print(f"Here is your change ${change}")
        clear()
        continue
    else:
        turn_on = False
        change = money_received
        print(f"Here is your change ${change} \n")
        print(f"Total profit is ${profit}")
        clear()
