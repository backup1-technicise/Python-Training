'''
Write a Python program to find urls in a string.
'''

import re
text = '<p>Contents :</p><a href="http://w3resource.com">Python Examples</a><a href="https://github.com">Even More Examples</a>'
#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
urls = re.findall('http[s]?://[\w]+\.[a-z]+', text)
print("Original string: ",text)
print("Urls: ", urls)