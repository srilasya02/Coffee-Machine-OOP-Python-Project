from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
c=CoffeeMaker()
money_machine=MoneyMachine()

is_on=True
#c.is_resource_sufficient(menuitem.name)

while is_on:
    options=menu.get_items()
    choice=input(f"what would you like?{options}")
    if choice=="off":
        is_on=False
    elif choice=="report":
        c.report()
        money_machine.report()
    else:
        choosen=menu.find_drink(choice)
        #print(choosen)
        if c.is_resource_sufficient(choosen):

            print(money_machine.make_payment(choosen.cost))
            c.make_coffee(choosen)

