'''
Write a Python program to match a string that contains only upper and lowercase letters, numbers and underscores.
'''

import re


def text_match(text):
        patterns = '^[a-zA-Z0-9_]+$'  # It represents that a String starts with an alphabet (Upper or lower character)or
        #  a digit or a underscore but it ends with an combination of alphabets, digits and under scores..
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return 'Not matched!'

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))