# from turtle import Turtle, Screen
#
# # https://docs.python.org/3/library/turtle.html
# # https://cs111.wellesley.edu/labs/lab01/colors
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# 找尋 python 的第三方套件
# https://pypi.org/

######################################################################################

# from prettytable import PrettyTable
#
# table = PrettyTable()
# print(table)
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l"
#
# print(table)

# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

######################################################################################

# Coffee Machine in OOP

from day016_menu import Menu, MenuItem
from day016_coffee_maker import CoffeeMaker
from day016_money_machine import MoneyMachine
menu = Menu()
is_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

