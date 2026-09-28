# This is day 15 of 100 days of Python
from time import sleep
from common.validators import validate_input, validate_int
from common.toolkit import clear_terminal
from .coffee_machine import CoffeeMachine


def main():
    choices = ["espresso", "latte", "capuccino", "report", "off"]
    ocm = CoffeeMachine()
    while True:
        ocm.print_menu()
        drink = validate_input(
            "What would you like? (espresso/latte/capuccino)\n - ", choices
        )
        if drink == "report":
            print(ocm.report())
            sleep(2)
        elif drink == "off":
            print("turning off...")
            sleep(1)
            break
        else:
            payment = "n"
            money = []
            while payment == "n":
                coin = validate_input(
                    "Input the coin your paying with: (penny/nickel/dime/quarter)\n - ",
                    ["penny", "dime", "quarter", "nickel"],
                )
                quantity = validate_int(f"How many {coin} are you putting in?\n - ")
                money.append({coin: quantity})
                payment = validate_input(
                    "Are you done? Type 'y' or 'n'\n - ", ["y", "n"]
                )
            ocm.make(drink, money)
            sleep(2)
        clear_terminal()


if __name__ == "__main__":
    main()
