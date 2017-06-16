'''

Assignment 13 : In a previous exercise, we have written a program that knows a number and asks a user to guess it.

This time, we are going to do exactly the opposite:-
1. You, the user, will have in your head a number between 0 and 100.
2. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
3. At the end of this exchange, your program should print out how many guesses it took to get your number.

Hints or logic :-
As the writer of this program, you will have to choose how your program will strategically guess.

a. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
But that is not an optimal guessing strategy.

b. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as
needed. After you have written the program, try to find the optimal strategy
(We will talk about what is the optimal one next week with the solution.)

'''


def Guess_a_Number(num_list, low, high, guess, in_user_head, tries):
    if low <= high:
        mid_index = (low + high) / 2
        guess = num_list[mid_index]     # set the initial guess based on strategy b.
        print "Computer guess: ", guess
        if guess == in_user_head:
            print("You Exactly Right! The number was", in_user_head)
            print("And it only took you", tries, "tries!\n")
        else:
            if guess > in_user_head:
                print("Too High... when guess > user_guess")
                tries += 1
                Guess_a_Number(num_list, low, mid_index - 1, guess, in_user_head, tries)
            else:
                print("Too Low... when guess < guess")
                tries += 1
                Guess_a_Number(num_list, mid_index + 1, high, guess, in_user_head, tries)

    else:
        print " Sorry !! User guess number not in the list 0 -100 ..."


print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 0 to 100.")
print("Computer !! try to guess it in as few attempts as possible.\n")

# set the user number in head
in_user_head = 60
guess = -99999       # Arbitrary Guess from Computer
tries = 1
Guess_a_Number(range(101), 0, len(range(101)) - 1, guess, in_user_head, tries)
''' Guess_a_Number = (a list of numbers 0 -100, list_low_index, list_high_index, arbitrary guess,
                    number in user head, num of tries) '''
raw_input("\n\nPress the enter key to exit.")
