'''
Write a Python program to replace maximum 2 occurrences of space, comma, or dot with colon
'''
import re
text = 'Python Exercises, PHP exercises.'
new_text = re.subn(r'[ \,\.]',':', text, 2)
print new_text
