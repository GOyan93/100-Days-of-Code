# The Coffee Machine
# Day 15 / 100: 100 Days of Code

import Data_Source

revenue = 0.0

def inquire_customer():
    requested_item = input(f" What would you like? (espresso (${Data_Source.MENU['espresso']['cost']})/latte (${Data_Source.MENU['latte']['cost']})/cappuccino(${Data_Source.MENU['cappuccino']['cost']})): ").lower()
    if requested_item in Data_Source.MENU:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        change_exchange(quarters, dimes, nickles, pennies, Data_Source.MENU[requested_item]['cost'], requested_item)
    elif requested_item == "report":
        report()
    elif requested_item == "off":
        print("Powering Off...")
    else:
        print("Sorry, that is not a valid selection.")
        inquire_customer()


def change_exchange(num_quaters, num_dimes, num_nickles, num_pennies, price, selected_item):
    global revenue
    total_deposited = 0.0
    total_deposited += round((num_quaters * 0.25), 2)
    total_deposited += round((num_dimes * 0.10), 2)
    total_deposited += round((num_nickles * 0.05), 2)
    total_deposited += round((num_pennies * 0.01), 2)
    print(f"Total deposited: ${total_deposited}")
    if total_deposited >= price:
        change = round(total_deposited - price, 2)
        revenue += price
        print(f"Here is your change: ${change}")
        ingredient_level_change(selected_item)
    else:
        print("Sorry that's not enough money. Money refunded.")
        inquire_customer()


def ingredient_level_change(menu_item):
    water_level = Data_Source.resources['water']
    milk_level = Data_Source.resources['milk']
    coffee_level = Data_Source.resources['coffee']
    water_required = Data_Source.MENU[menu_item]['ingredients']['water']
    milk_required = Data_Source.MENU[menu_item]['ingredients']["milk"]
    coffee_required = Data_Source.MENU[menu_item]['ingredients']['coffee']

    if water_required > water_level:
        print("Sorry there is not enough water.")
        inquire_customer()
    if milk_required > milk_level:
        print("Sorry there is not enough milk.")
        inquire_customer()
    if coffee_required > coffee_level:
        print("Sorry there is not enough coffee.")
        inquire_customer()
    else:
        print(f"Here is your {menu_item} ☕️. Enjoy!")
        water_level -= water_required
        Data_Source.resources['water'] = water_level
        milk_level -= milk_required
        Data_Source.resources['milk'] = milk_level
        coffee_level -= coffee_required
        Data_Source.resources['coffee'] = coffee_level
        inquire_customer()


def report():
    global revenue
    remaining_water = Data_Source.resources['water']
    remaining_milk = Data_Source.resources['milk']
    remaining_coffee = Data_Source.resources['coffee']

    print(f"Water: {remaining_water}")
    print(f"Milk: {remaining_milk}")
    print(f"Coffee: {remaining_coffee}")
    print(f"Money: ${revenue}")
    inquire_customer()

inquire_customer()
