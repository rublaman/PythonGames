from data import MENU, resources


def turn_off() -> None:
    print("Turning off Coffee Machine")


def check_option(user_input: str, resources_machine: dict, money: float) -> None:
    if user_input == "off":
        turn_off()
    elif user_input == "report":
        print_report(resources_machine, money)
        run_machine(resources_machine, money)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        make_coffee(resources_machine, user_input, money)


def print_report(resources_machine: dict, money: float) -> None:
    print(
        f'Water: {resources_machine["water"]}ml'
        f'\nMilk: {resources_machine["milk"]}ml'
        f'\nCoffee: {resources_machine["coffee"]}g'
        f'\nMoney: ${money}'
    )


def check_resources(resources_machine: dict, coffee: str) -> list:

    enough_resources = []
    for ingredient in MENU[coffee]["ingredients"]:
        if resources_machine[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            enough_resources.append(ingredient)

    return enough_resources


def process_coins(coffee: str) -> int:
    print("Please, insert coins.")
    quarters = float(input("hoy many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    total = total - MENU[coffee]["cost"]

    return total


def check_transaction(resources_machine: dict, coffee: str) -> dict:
    for ingredient in MENU[coffee]["ingredients"]:
        resources_machine[ingredient] = resources_machine[ingredient] - MENU[coffee]["ingredients"][ingredient]

    return resources_machine


def make_coffee(resources_machine: dict, coffee: str, money: float):
    enough_resources = check_resources(resources_machine, coffee)
    if len(enough_resources) == 0:
        total_money = process_coins(coffee)
        if total_money > 0:
            money += MENU[coffee]["cost"]
            resources_machine = check_transaction(resources_machine, coffee)


            print(f"Here is your {coffee}☕. Enjoy!")
            run_machine(resources_machine, money)
    else:
        lack_resources = ', '.join(enough_resources)
        print(f"Sorry, the next resources are not enough: {lack_resources}")


def run_machine(resources_machine: dict, money: float):
    user_input = input("What would you like? (espresso/latte/cappuccino) ")
    check_option(user_input, resources_machine, money)


run_machine(resources, 0)
