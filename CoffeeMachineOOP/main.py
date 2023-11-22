from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_machine = CoffeeMaker()
money_process = MoneyMachine()
menu = Menu()

machine_status = True

while machine_status:

    user_input = input("What would you like? (latte / espresso / cappuccino) ")

    if user_input == "report":
        coffe_machine.report()
        money_process.report()
    elif user_input in menu.get_items():
        menu_selected: MenuItem = menu.find_drink(user_input)
        is_resource_sufficient = coffe_machine.is_resource_sufficient(menu_selected)

        if is_resource_sufficient:
            is_payment_successful = money_process.make_payment(menu_selected.cost)
            if is_payment_successful:
                coffe_machine.make_coffee(menu_selected)
    elif user_input == "off":
        machine_status = False
        print("Turning off Coffee Machine")
