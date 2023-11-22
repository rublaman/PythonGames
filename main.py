from CoffeeMachine.main import start as coffee_machine
from CoffeeMachineOOP.main import start as coffee_machine_oop

print("1. CoffeeMachine")
print("2. CoffeeMachineOOP")
print("3. TO-DO")

user_option = input("What project do you want to test? (Insert number) ")

match user_option:
    case "1":
        coffee_machine()
    case "2":
        coffee_machine_oop()
    case "3":
        print("TO-DO")
    case _:
        print("Bye!")

print("HI")