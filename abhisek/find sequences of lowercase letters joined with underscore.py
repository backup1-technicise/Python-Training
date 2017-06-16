'''
Write a Python program to find sequences of lowercase letters joined with underscore.
'''
import re


def text_match(str):
    match = re.search(r'\w*[a-z]{1}_[a-z]{1}\w*', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))