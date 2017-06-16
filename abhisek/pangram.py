'''
Assignment 18: A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: the quick brown fox jumps over the lazy dog
Your task here is to write a function to check a sentence to see if it is a pangram or not.
'''
import string


def check_Pengram(Str):
    flag = False        # Flag for checking pengram
    new_str = ''
    for Char in Str:
        if Char != " ":
            new_str += Char
    #print new_str

    Eng_alphabet_List = list(string.ascii_lowercase)
    Given_alphabet_list = list(new_str)
    for Char in Eng_alphabet_List:
        if Char not in Given_alphabet_list:
            print "Given String is not Pengram"
            flag = False
            break
        else:
            flag = True
    if flag == True:
        print "Given String is Pengram"

Str = raw_input("Enter a String for pengram checking: ")
print "Given String : ", Str
print "Is String %s is a Pengram? : " % Str,
check_Pengram(Str)