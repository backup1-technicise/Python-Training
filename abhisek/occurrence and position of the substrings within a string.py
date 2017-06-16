'''
Write a Python program to find the occurrence and position of the substrings within a string.
'''

import re
text = 'Python exercises, PHP exercises, C# exercises'
given_string = raw_input("Enter a string to search in text:")
for string in re.finditer(given_string, text):
    print "Given String:%s from index %d to index %d" %(given_string, string.start(), string.end())
