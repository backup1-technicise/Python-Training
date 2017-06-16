'''
Write a Python program to remove the ANSI escape sequences from a string.
'''

import re
text = "PHP Exercises\tMySQL Exercises\nAlgo Exercises\r"


print("Original Text: ", text)
new_text1 = re.sub(r'[\n|\t|\r]+', r'. ', text)
print("New Text: ", new_text1)
