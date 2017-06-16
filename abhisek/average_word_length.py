'''
Assignment 38 : Write a program that will calculate the average word length of a text stored in a file (i.e the sum of
all the lengths of the word tokens in the text, divided by the number of word tokens).
'''

import nltk
fp = open("Token.txt", "r")
file_content = fp.read()
print file_content
print type(file_content)
print len(file_content)

tokens = nltk.word_tokenize(file_content)  # Identify token from raw file content
print tokens
print type(tokens)
print len(tokens)
print tokens[:21]    # First 20 tokens

print "***************************************************************************************************************"
each_token_length = dict()  # holds length of each token
for token in tokens:
    each_token_length[token] = len(token)

total_length_of_token = 0
for token in tokens:
    total_length_of_token += each_token_length[token]
print "Total token length:", total_length_of_token
print "Tokens with length:", each_token_length
print "Total tokens:", len(tokens)
average_word_length = float(total_length_of_token) / len(tokens)
print "Average word length is : %f" % average_word_length
