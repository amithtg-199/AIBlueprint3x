from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_start = True

while is_start:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").strip().lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_start = False
        continue
    else:
        menue_item = menu.find_drink(choice)
        if menue_item is not None:
            if coffee_maker.is_resource_sufficient(menue_item) and money_machine.make_payment(menue_item.cost):
                coffee_maker.make_coffee(menue_item)

