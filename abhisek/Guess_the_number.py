'''
Assignment 39 : Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly
chosen between 1 and 20. (Source: http://inventwithpython.com)
'''

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 20.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 20)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower... when guess > the_number")
    else:
        print("Higher... when guess < the_number")

    guess = int(input("Take a guess: "))
    tries += 1
    if tries == 10:
        print "You failed to guess in time!"
        break
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")

raw_input("\n\nPress the enter key to exit.")
