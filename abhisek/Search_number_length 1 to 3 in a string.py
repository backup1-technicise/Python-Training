'''
Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
'''

import re
text = "Exercises number 1, 12, 13, and 345 are important"
List = re.findall(r'\b\d{1,3}\b', text)
print List
