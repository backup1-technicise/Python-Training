'''
Write a Python program to check for a number at the end of a string.
'''
import re
Str_list = ['abcdef', 'abcdef6']
for string in Str_list:
    match = re.search(r'\w+\d',string)
    if match:
        print match.group()
    else:
        continue
