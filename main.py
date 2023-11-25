from CoffeeMachine.main import start as coffee_machine
from CoffeeMachineOOP.main import start as coffee_machine_oop
from QuizGame.main import start as quiz_game
from HirsPainting.main import start as hirs_painting
from TurtleRace.main import start_race as turtle_race


print("1. Coffee Machine")
print("2. Coffee Machine OOP")
print("3. Quiz Game")
print("4. Hirs Painting")
print("4. Turtle Race")

user_option = input("What project do you want to test? (Insert number) ")

match user_option:
    case "1":
        coffee_machine()
    case "2":
        coffee_machine_oop()
    case "3":
        quiz_game()
    case "4":
        hirs_painting()
    case "5":
        turtle_race()
    case _:
        print("Bye!")
