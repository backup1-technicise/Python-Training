'''
Write a Python program to match if two words from a list of words starting with letter 'P'.
'''
import re
# Sample strings.
words = ["Python PHP", "Java JavaScript", "c c++"]
for word in words:
    match = re.search(r'(P\w+)\s{1,}(P\w+)', word)
    if match:
        print "First word:"
        print match.group(1)
        print "Second word:"
        print match.group(2)
