'''
Write a Python program to separate and print the numbers of a given string.
'''
import re
text = "Ten 10, Twenty 20, Thirty 30"
Num_list = re.findall(r'\b\d+\b', text)
print "Numbers of a given string:"
print Num_list
