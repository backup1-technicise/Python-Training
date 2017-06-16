'''
Assignment 36: A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written
record of a language, the works of an author, or in a single text. Define a function that given the file name of a text
will return all its hapaxes. Make sure your program ignores capitalization.
'''

import nltk
#nltk.download()
from nltk.book import *
from urllib import urlopen

Length_text5 = len(text5)
print "Length_text3", Length_text5
print text5[:10]
text_content = [word for word in text5]
print text_content
fdist5 = FreqDist(text5[:10])
print fdist5
print fdist5.hapaxes()
for key, value in fdist5.iteritems():
    print key, "Occours", value, "times"
print texts()


