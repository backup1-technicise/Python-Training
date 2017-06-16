'''
Write a Python program that matches a word containing 'z', not start or end of word.
'''

import re

def text_match(String):
    match = re.search(r'\b\w+z\w+\b', String)
    if match:
        print "Word is :", match.group()
        return True
    else:
        return False

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))