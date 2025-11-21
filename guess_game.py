#Have to ask to guess a number between 0-100
#if its anything above 100 or not 100 i have to return please enter valid number

import random
while True:
    user_input = int(input("Guess the number between 1 and 100: "))
    chosen_number = 8

    if user_input > chosen_number:
        print("Too high")
    elif user_input < chosen_number:
        print("Too low!")
    elif user_input == 8:
        print("Congratulations! You guessed the number.")
        break
    else:
        if user_input > 100 and user_input < 1:
            print("Please enter a valid number")
        
print()

    