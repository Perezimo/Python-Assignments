#Guessing number game...

import random
guess_number = 455
user_guess = int(input("Guess my number between 1 and 1000 with the fewest guess: "))

number = random.randint(1, 1000)
while user_guess != guess_number:
        if user_guess > 1000:
            print("Hey, number must be between 1 and 1000")
        if user_guess > 500 and user_guess <= 1000:
            print("Too high, try again!!!")
        if user_guess <400:
            print("Too low, try again!!!")
        user_guess = int(input("Guess my number between 1 and 1000 with the fewest guess: "))

        if user_guess == guess_number:
    
            print("congratulations")
    
