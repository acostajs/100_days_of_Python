# This is Day 2 of 100 days of Python

"""
This script runs the code for day 2 of 100 days of Python.
It propmts the percentage choosen for tipping and the amount of people to split the bill with,
then prints a sentence with the amount of tip and total bill to pay per person.
"""
def calculate_tip(bill, tip_percentage, people):
    tip = (bill * tip_percentage) / people
    return round(tip, 2)

def calculate_total_bill(bill, tip_percentage, people):
    total_bill = ((bill * tip_percentage) + bill) / people
    return round(total_bill, 2) 

def main():
    name = input("Hi! what is your name? : ")
    print(f"Hi! {name}, let's calculate how much you have to pay for the tip\nAnswer the following questions")
    bill = float(input("What was the bill? $"))
    tip_percentage = float(input("How much tip would you like to give? 10, 15, maybe 20? %")) / 100
    people = int(input("How many people to split the bill with? "))
    tip = calculate_tip(bill, tip_percentage, people)
    total_bill = calculate_total_bill(bill, tip_percentage, people)
    print(f"{name}, the tip is ${tip} and your total bill is ${total_bill}")

if __name__ == "__main__":
    main()
 
