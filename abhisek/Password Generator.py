'''Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of
lowercase letters,
uppercase letters,
numbers, and
symbols.

The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main() method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import numpy as np
import string
import math


def Strong_Passwd():
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    numbers = [str(y) for y in range(0, 10)]
    X = [x for x in string.printable if x not in lowercase_letters and x not in uppercase_letters and x not in numbers]
    symbols = [S for S in X if S not in ('\t', '\n', '\r', '\x0b', '\x0c')]
    print symbols

    check_flag = False
    while not check_flag:
        passwd_len = int(input("Enter the length of the password:"))
        n_lower = int(input("Enter the no. of lower chars in password:"))
        n_upper = int(input("Enter the no. of upper in password:"))
        n_digit = int(input("Enter the no. of digits in password:"))
        n_symbol = int(input("Enter the no. of symbols in password:"))
        if (n_lower + n_upper + n_digit + n_symbol) == passwd_len:
            check_flag = True
        else:
            print "Sorry!!, No. of characters exceeds the given length of password !!!! \n\n"

    strong_password = "".join(np.random.choice(lowercase_letters, n_lower, replace=False)) + "".join(np.random.choice(uppercase_letters, n_upper, replace=False)) \
           + "".join(np.random.choice(numbers, n_digit, replace=False)) + "".join(np.random.choice(symbols, n_symbol, replace=False))


    print "Your randomly generated Strong password is :", strong_password


def Weak_Passwd():
    #  For weak passwords, pick a word or two from a list.
    fp = open("unixdict.txt", "r")
    #print "File's content : ", fp.read()
    fp.seek(0)
    Word_list = list()
    for word in fp:
        word = word.strip('\n')
        Word_list.append(word)
    print "Your word list is : "
    print Word_list

    passwd_len = int(input("Enter the length of the password:"))
    passwd_first_part = math.ceil(passwd_len / 2)
    passwd_second_part = math.floor(passwd_len / 2)

    weak_password = ''

    for word1 in Word_list:
        if len(word1) == passwd_first_part:
            weak_password += word1
            break

    for word2 in Word_list:
        if len(word2) == passwd_second_part and word2 != weak_password:
            weak_password += word2
            break

    print "Your weak password is :", weak_password


def Option(user_option):
    Call_function = {1: Weak_Passwd, 2: Strong_Passwd}
    Call_function[user_option]()

user_option = int(input(" Press 1 to get Weak Paswword and Press 2 for Strong Password:"))
Option(user_option)
