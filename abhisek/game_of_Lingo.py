'''
Assignment 41 :

In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by
guessing, and in return receive two kinds of clues:
1) the characters that are fully correct, with respect to identity as well as to position, and
2) the characters that are indeed present in the word, but which are placed in the wrong
position.
Write a program with which one can play Lingo.
Use square brackets to mark characters correct in the sense of 1), and
ordinary parentheses to mark characters correct in the sense of 2).

Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the
following way:

snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]

'''


def clue(hidden_word, user_guess):
    guess_word_list = list(user_guess)
    hidden_word_list = list(hidden_word)
    matched_word = list()
    position = list()
    match_word_position = list()

    for Char in guess_word_list:
        if Char in hidden_word_list:  # if Char in guess word presents in word list of hidden word.
            matched_word.append(Char)   # matched word is stored.
            index = guess_word_list.index(Char)
            position.append(index)    # position of matched word is stored.

        else:
            matched_word.append(' ')   # unmatched word is ' '.
            index = guess_word_list.index(Char)
            position.append(index)    # position of matched word is stored.


    for pos in position:
        if hidden_word_list[pos] == matched_word[pos]:      # Position wise matching.
            match_word_position.append(matched_word[pos])   # add position wise matched char.

    clue_word = ''
    for Char in user_guess:
        if Char in match_word_position:
            clue_word += "[" + Char + "]"
        elif Char not in match_word_position and Char in matched_word:
            clue_word += "(" + Char + ")"
        else:
            clue_word += Char

    del guess_word_list
    del hidden_word_list
    del matched_word
    del position
    del match_word_position

    return clue_word

print("\tWelcome to game of Lingo is a type of word play'!")
print("There is a hidden word, five characters long and your need to in few attempts as possible.\n")
print("\t Guess First then you get two clues such as :- \n 1. the characters that are fully correct, with respect to identity as well as to position\n")
print(" 2.the characters that are indeed present in the word, but which are placed in the wrong position.\n\n")
hidden_word = "tiger"
guess = raw_input("Guess the word: ")
word_clue = clue(hidden_word, guess)
print word_clue
tries = 1
option_flag = False
# Selected Color guessing loop from Anagram
while guess != hidden_word:
    if tries == 4:          # 4 attempts to say actual color from anagram
        print "You failed to guess in time!"
        print "The word was", hidden_word
        option_flag = True
        break
    else:
        if guess == hidden_word:
            print("Oh! You guessed it! The hidden word was", hidden_word)
            print("And it only took you", tries, "tries!\n")
            option_flag = True
            break
        else:
            tries += 1
            guess = raw_input("Guess the word: ")
            word_clue = clue(hidden_word, guess)
            print word_clue

if not option_flag:
    print "Oh! You guessed it! TheHidden word was: ", hidden_word
