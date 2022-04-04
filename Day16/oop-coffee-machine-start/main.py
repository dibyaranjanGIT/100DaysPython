from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if menu.check_drink(choice):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
