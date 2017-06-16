'''
Write a Python program to split string with multiple delimiters.
'''

import re
text = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('[;,\*\n]', text))    # Another similar pattern is ';|\*|\,|\n'
