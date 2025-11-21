import random


while True:
    dice_input = input("Roll the dice? (y/n): ").lower()
    if dice_input == "y":

        random_int1 = random.randint(1,6)
        random_int2 = random.randint(1,6)

        print( (random_int1, random_int2))
    elif dice_input == "n":
     print("Thanks for playing")
     break 
    else:
       print("Invalid choice!")
    


