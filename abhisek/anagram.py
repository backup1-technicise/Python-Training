'''
Assignment 40 : An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce
a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse,
A decimal point = I'm a dot in place. Write a Python program that, when started
1) randomly picks a word w from given list of words,
2) randomly permutes w (thus creating an anagram of w),
3) presents the anagram to the user, and
4) enters an interactive loop in which the user is invited to guess the original word.

Note : It may be a good idea to work with (say) colour words only.
'''

import random
import numpy as np
random.seed(42)


def Create_Anagram(Color_string):
    Color = list(Color_string)    # String to List conversion
    while True:
        random_swaps = np.random.choice(len(Color) / 2, 1, replace=False)   # Choose 1 - len(color) / 2 number of swaps for each Anagram
        #print random_swaps
        for swaps in range(random_swaps):
            x1, x2 = np.random.choice(range(0, len(Color)), 2, replace=False) # For each swap choose two random points in a Color
            #print x1, x2
            temp = Color[x1]
            Color[x1] = Color[x2]
            Color[x2] = temp

        anagram = ''.join(Color)
        if anagram != Color_string:
            break
    return anagram


Color_list = ["DarkBlue", "green", "navyblue", "deepskyblue", "springgreen", "turquoise", "honeydew", "lightseagreen",
             "mediumspringgreen", "paleturquoise", "darkmagenta", "mediumvioletred", "darkolivegreen"]

print("\tWelcome to 'An anagram is a type of word play'!")
print("Try to guess actual Color from Anagram in few attempts as possible.\n")

# Select a random color from Color List
select_color_index = np.random.choice(range(0, len(Color_list)), 1, replace=False)
Color = Color_list[select_color_index]
tries = 1
Anagram = Create_Anagram(Color)
print"Colour word anagram:", Anagram
guess = raw_input("Guess the color: ")

# Selected Color guessing loop from Anagram
while guess != Anagram:
    if tries == 4:          # 4 attempts to say actual color from anagram
        print "You failed to guess in time!"
        print "The Color was", Color
        break
    else:
        if guess == Color:
            print("You guessed it! The Color was", Color)
            print("And it only took you", tries, "tries!\n")
            break
        else:
            tries += 1
            Anagram = Create_Anagram(Color)
            print"Colour word anagram:", Anagram
            guess = raw_input("Guess the color: ")




