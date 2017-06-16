'''
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
'''

import re

def is_allowed_specific_char(str):
    match = re.search(r'^[a-zA-Z0-9][a-zA-Z0-9]*$',str)
    if match:
        print "The matched string is :", match.group()
        return True
    else:
        print "The given string is not matched"
        return False
print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))