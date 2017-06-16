'''
Assignment 33 : According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase
backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file
name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the
screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the
pair "stressed desserts".
Note, by the way, that each pair by itself forms a palindrome!
'''

import enchant   # PyEnchant is a spellchecking library for Python, based on the excellent Enchant library.


def check_Plaindrome(input_String):
    new_input_String = ''
    for Char in input_String:
        if Char not in (",", "'", ".", " ", "?", "!"):   # Removal of special characters from String
            new_input_String += Char

    List = list(new_input_String)
    for i in range(len(List)):
        if List[i].isupper():
            List[i] = List[i].swapcase()
    new_input_String = ''.join(List)


    ''' Palindrome Checking Operation..'''
    length = len(new_input_String)
    check_flag = 0
    for i in range(0, length/2):  # Checking front to middle characters
        j = length - i - 1  # Checking back to middle characters
        char_i = new_input_String[i]
        char_j = new_input_String[j]
        if char_i != char_j:
            check_flag = 0
            break
        else:
            check_flag = 1
    if check_flag == 0:
        return False
    else:
        return True


def check_Semordnilap(Line):
    reverse_Line = ''
    Palindrome_reverse_Line = ''
    for i in range(len(Line) - 1, - 1, -1):
        reverse_Line += Line[i]
    if reverse_Line != Line:
        d = enchant.Dict("en_US")  # Word Validity is Based on US English Dictionary.
        if d.check(reverse_Line):  # If Semordnilap is a valid word in US English
            Palindrome_reverse_Line = Line + " " + reverse_Line
            Status = check_Plaindrome(Palindrome_reverse_Line)
            if Status:  # if a word and its reverse is a palindrome
                print Palindrome_reverse_Line
        else:  # If Semordnilap is not a vaild word in US English
            print"%s is not a valid word in US English Dictionary"% reverse_Line


fp = open("semordnilap.txt", "r")
for Line in fp:
    Line = Line.strip("\n")
    print "Current semordnilap from file : ", Line
    check_Semordnilap(Line)
