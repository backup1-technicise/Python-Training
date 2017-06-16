'''
 Write a Python program for Sequential search.
'''

import numpy


def Sequential_Search(num_list, low, high, X):
    element_found = False
    for i in range(low, high + 1):
        element = num_list[i]
        if element == X:
            print "Element %d has been found at position = %d." % (X, i + 1)
            element_found = True
            break
    if not element_found:
        print "Element %d has not been found in num_list." % X


print("\tCode for 'Sequential Search'!")
# Generate 10 random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 10, replace=False))
print "Randomly generated numbers list: "
print element_list
X = int(input("Enter an element to search over list : "))

Sequential_Search(element_list, 0, len(element_list) - 1, X)
