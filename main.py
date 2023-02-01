from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
import art

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_banner = PrettyTable()
banner_logo = [art.logo, art.welcome]
coffee_banner.add_column("Coffee Machine",banner_logo)

def run_coffee():
    print(coffee_banner)
    action = input("What would you like to do? \n - order coffee \n - read report \n - restock \n - turn off \n").lower()
    displayed_menu = menu.get_items()
    menu_table = PrettyTable()
    table_list = [displayed_menu]

    if action == "order coffee":
        menu_table.add_column("----- Menu -----", table_list)
        print(menu_table)
        print(" ")
        order = input("What would you like to order? \n").lower()
        print(" ")
        drink = menu.find_drink(order_name=order)
        check_resource = coffee_maker.is_resource_sufficient(drink=drink)
        if check_resource:
            print(f"Your {drink.name} costs ${drink.cost}. Please pay in coins.")
            print(" ")

            if money_machine.make_payment(drink.cost):

                coffee_maker.make_coffee(drink)
                print(" ")
                print("Thank you for your order!")
                print(" ")

                run_coffee()
            else:
                print("Sorry, not enough money! Please try again later.")
                run_coffee()


        else:
            print("Sorry, not enough resources. Try again later.")
            run_coffee()

    elif action == "read report":
        print(" ")
        print("Current Status:")
        coffee_maker.report()
        print(" ")
        print("Money Made:")
        money_machine.report()
        print(" ")
        run_coffee()
    elif action == "turn off":
        print("Goodbye")
    elif action == "restock":
        coffee_maker.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        run_coffee()
    else:
        print("Sorry, that is not a valid option. Please try again.")
        run_coffee()

run_coffee()