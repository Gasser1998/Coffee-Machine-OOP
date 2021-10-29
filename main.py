
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

def Coffee():
    power = True
    while power == True:
        options = menu.get_items()
        user_choice = input(f"What would you like to order ({options}): ")
        if user_choice == "off":
            print('Goodbye')
            exit()
        elif user_choice == "report":
            machine.report()
            money.report()
            Coffee()
        else:
            drink = menu.find_drink(user_choice)
            enough = machine.is_resource_sufficient(drink)
            if enough is True:
                user_money = money.make_payment(drink.cost)
                if user_money == True:
                    machine.make_coffee(drink)
                else:
                    Coffee()
            else:
                Coffee()


Coffee()

