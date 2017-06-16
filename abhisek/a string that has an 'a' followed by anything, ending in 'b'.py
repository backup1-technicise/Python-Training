'''
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
'''

import re

def text_match(str):
    match = re.search(r'^(a|\w*a)\w*b$', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

print(text_match("aabbbbc"))
print(text_match("aabAbbbc"))
print(text_match("ABCDEF"))
