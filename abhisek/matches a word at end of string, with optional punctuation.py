'''
Write a Python program that matches a word at end of string, with optional punctuation.
'''

import re


def text_match(text):
        match = re.search(r'(\w+\W*)$', text)  # In this way if we add ^ then the pattern matches a word at beginning.
        if match:
            print "word is :", match.group()
            return 'Found a match!'
        else:
                return 'Not matched!'

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))
