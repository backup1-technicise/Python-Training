'''
 Write a Python program to search some literals strings in a string.
'''

import re
Sample_text = 'The quick brown fox jumps over the lazy dog.'
''' Searched words : 'fox', 'dog', 'horse'''
for word in re.finditer(r'\b\w{3,5}\b', Sample_text, re.IGNORECASE):
    if word.group() in ['fox', 'dog', 'horse']:
        print "%s" % word.group(), "found at index:", word.start()

