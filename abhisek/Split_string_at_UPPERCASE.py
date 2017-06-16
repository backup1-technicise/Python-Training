'''
Write a Python program to split a string at uppercase letters.
'''

import re
text = "php Eexercises MmySsequel EexercisesAalgo Eexercises"
print("Original Text: ", text)
# new_text = re.split(r'[A-Z]', text, 3)  # Maximum 3 splits at UPPERCASE letter
new_text = re.split(r'[A-Z]', text)  # Splits at UPPERCASE letters
print "New Text: ", new_text

