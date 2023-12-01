from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print(Menu.logo)
menu = Menu()
money = MoneyMachine()
coffee_machine = CoffeeMaker()
while True:
    n = input(f'What would you like {menu.get_items()} : ')
    if n == 'off':
        print("Thank-you for using our coffee machine")
        print(Menu.logo)
        break
    if n == 'report':
        coffee_machine.report()
        money.report()
        continue
    item = menu.find_drink(n)
    if item == None:
        continue
    else:
        if not coffee_machine.is_resource_sufficient(item) :
            continue
        else:
            print(item.cost)
            if money.make_payment(cost=item.cost):
                coffee_machine.make_coffee(item)