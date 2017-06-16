'''
Write a Python program to find all adverbs and their positions in a given sentence.
'''

import re
text = "Clearly, he has no excuse for such behavior."
for m in re.finditer(r".+ly", text):         # Equivalent pattern r'\w+ly'
    print('%d-%d: %s' % (m.start(), m.end(), m.group()))

