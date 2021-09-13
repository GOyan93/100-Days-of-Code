from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_5000 = CoffeeMaker()
money_exchanger = MoneyMachine()
item_inventory = Menu()



on = True
while on:
    requested_item = input(f" What would you like? ({item_inventory.get_items()}): ")
    if requested_item.lower() == "off":
        on = False
    elif requested_item.lower() == "report":
        coffee_maker_5000.report()
        money_exchanger.report()
    else:
        prepared_drink = item_inventory.find_drink(requested_item)
        if coffee_maker_5000.is_resource_sufficient(prepared_drink):
            money_exchanger.make_payment(prepared_drink.cost)
            coffee_maker_5000.make_coffee(prepared_drink)





