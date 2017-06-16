'''
Assignments 5 : Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (dont worry if you cant figure this out at this point - well get to it soon)

'''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = [element for element in b if element in a]
print "common_elements"
print common_elements

''' Extra  part'''

A = range(random.randint(1, 10))
print "Random List A:"
print A
B = range(random.randint(1, 15))
print "Random List B:"
print B
Common_elements = [element for element in B if element in A]
print "Common Element list:"
print Common_elements
