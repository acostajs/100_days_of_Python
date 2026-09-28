from common.common_art import COMMON_ART
from .task_art import TASK_ART


class CoffeeMachine:
    def __init__(self, water: int = 300, coffee: int = 100, milk: int = 200):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.money_collected = 0
        self.recipes = {
            "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 150},
            "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 250},
            "capuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 300},
        }
        self.coins = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}

    def print_menu(self):
        print(TASK_ART["title"])
        print(TASK_ART["machine"])
        print(COMMON_ART["divider"])

        for name, details in self.recipes.items():
            print(f"{name}: ${(details['price'] / 100):.2f}")

        print(COMMON_ART["divider"])

    def check_resources(self, drink: str) -> bool:
        recipe = self.recipes[drink]
        missing = []
        if self.water < recipe["water"]:
            missing.append("water")
        if self.coffee < recipe["coffee"]:
            missing.append("coffee")
        if self.milk < recipe["milk"]:
            missing.append("milk")

        if missing:
            print(f"Sorry, there is not enough {' ,'.join(missing)}")
            return False

        return True

    def calculate_value(self, coin: str, quantity: int) -> float:
        value = self.coins[coin] * quantity
        return value

    def check_payment(self, drink: str, money: list[dict]):
        recipe = self.recipes[drink]
        total = 0
        for coin in money:
            coin_name, quantity = next(iter(coin.items()))
            total += self.calculate_value(coin_name, quantity)

        if recipe["price"] > total:
            print("Sorry, that is not enough money. Money refunded.")
            return False

        change = round(total - recipe["price"], 2)
        if change > 0:
            print(f"Here is {(change / 100):.2f} in change.")
        return True

    def make(self, drink: str, money):
        """Make drink after checking resources, and take payment."""
        if self.check_resources(drink) and self.check_payment(drink, money):
            recipe = self.recipes[drink]
            self.water -= recipe["water"]
            self.coffee -= recipe["coffee"]
            self.milk -= recipe["milk"]
            self.money_collected += recipe["price"]
            print(TASK_ART[drink])
            print(f"Here is your {drink}, enjoy!")

    def report(self):
        return f"Water: {self.water}ml\nCoffee: {self.coffee}gr\nMilk: {self.milk}ml\nMoney: {(self.money_collected / 100):.2f}"
