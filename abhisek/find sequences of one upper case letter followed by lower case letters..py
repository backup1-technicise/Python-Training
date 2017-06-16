'''
Write a Python program to find sequences of one upper case letter followed by lower case letters.
'''

import re


def text_match(str):
    match = re.search(r'([A-Z]|\w+[A-Z])[a-z]+', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))