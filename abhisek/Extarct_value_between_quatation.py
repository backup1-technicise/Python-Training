'''
Write a Python program to extract values between quotation ' ' marks of a string.
'''

import re
text1 = '"Python", "PHP", "Java"'
print(re.findall(r'\w+', text1))
