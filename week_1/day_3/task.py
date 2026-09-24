# This is Day 3 of 100 days of Python

"""
This script runs the code for day 3 of 100 days of Python.
It prompts a series of questions to determine if the user wins the game or looses.

"""

def main():
    print("Welcome to Treasure Island.\nYour mission is to find the treasure\n ---------------")

    first_move = input("You're at a cross road. Where do you want to go?\n - Type 'left' or 'right'\n - ").lower()
    if first_move != "left":
        print("You FELL into a hole\n..GAME OVER..")
        return

    second_move = input("You've come to a lake. There is an island in the middle of the lake.\n - Type 'wait' to wait for a boat.\n - Type 'swim' to swim across.\n - ").lower()
    if second_move != "wait":
        print("You were ATTACKED by an evil Trout!.\n..GAME OVER..")
        return

    third_move = input("You arrive at the island unharmed.\nThere is a house with 3 doors. One red, one yellow, one blue.\n Which color do you choose?\n - ").lower()
    if third_move != "red":
        print("You were EATEN by evil beasts!.\n..GAME OVER..")
        return
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
          ''')
    print("You WIN! You have found the TREASURE!")        

if __name__ == "__main__":
    main()
