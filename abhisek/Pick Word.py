'''
Assignment 14 : In this exercise, the task is to write a function that picks a random word from a list of words from the
SOWPODS dictionary. Download this file and save it in the same directory as your Python code. Each line in the file
contains a single word.
'''


import numpy as np

fp = open("sowpods.txt", "r")
word_list = list()
for word in fp:
    word_list.append(word)
    
while len(word_list) != 0:
    random_word = "".join(np.random.choice(word_list, 1, replace=False))
    print "Randomly selected word: ", random_word
    random_word_index = word_list.index(random_word)
    del word_list[random_word_index]

print "Word list length :", len(word_list)
