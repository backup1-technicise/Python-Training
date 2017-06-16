'''
 Write a Python program for binary search.
'''

import numpy


def Binary_Search(num_list, low, high, X):
    if low <= high:
        mid_index = (low + high) / 2
        if X == num_list[mid_index]:
            print("Oh! The number is found !!! ")
            print(" The number is = %d at index = %d" % (X, mid_index + 1))
        else:
            if X < num_list[mid_index]:
                Binary_Search(num_list, low, mid_index - 1, X)
            else:
                Binary_Search(num_list, mid_index + 1, high, X)

    else:
        print " Sorry !! number X is not in list ..."


print("\tCode for 'Binary Search'!")
# Generate 10 random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 10, replace=False))
print "Randomly generated numbers list: "
print element_list
X = int(input("Enter an element to search over list : "))
element_list.sort()
print "Ordered elements list:"
print element_list
Binary_Search(element_list, 0, len(element_list) - 1, X)
