'''
Write a Python program to remove everything except alphanumeric characters from a string.
In some usages, the alphanumeric character set may include both upper and lower case letters, punctuation marks,
and symbols (such as @, &, and *, for example).

given Text : '**//Python Exercises// -@ 12 3- 4&.. '
'''

import re
text = '**//Python Exercises// -@ 12 3- 4&.. '


print "Original Text: ", text
new_text = re.sub(r'[A-Z|a-z|\@|\&|\*]+', '', text)
print "New Text: ", new_text
