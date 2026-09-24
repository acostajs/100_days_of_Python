# This is the task for Day 10 of 100 days of Python


from helpers import validate_int, validate_choice, calc
from ascii_art import ascii_art

def main():
    calculator = "on"
    previous_calc = "no"
    result = 0

    print(ascii_art("title"))
    print(ascii_art("divider"))
    while calculator == "on":
        if previous_calc == "yes":    
            first_number = result
        else:
            first_number = validate_int("What's the first number:\n - ")
            
        operator = validate_choice({"+", "-", "*", "/" }, input("+ - * / \nPick an operation:\n - "))
        second_number = validate_int("What's the second number:\n - ")

        try:         
            result = calc(operator, first_number, second_number)
        except ValueError as error:
            print(f"Error: {error}")
            return
        print(f"{first_number} {operator} {second_number} = {result}")
        print(ascii_art("divider"))
        print(f"Type 'y' to continue calculating with {result}")
        print("Type 'n' to start a new calculation")
        print("Type 'esc' to quit the calculator")
        continue_or_not = validate_choice({"y", "n", "esc"}, input(" - ").lower())
        print(ascii_art("divider"))
        

        if continue_or_not == 'y':
            previous_calc = 'yes'
        elif continue_or_not == 'n':
            previous_calc = 'no'
        elif continue_or_not == 'esc':
            calculator = 'off'



if __name__ == "__main__":
    main()
