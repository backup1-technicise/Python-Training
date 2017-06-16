'''
Write a Python program to sort a list of elements using the insertion sort algorithm.
'''

import numpy

def Insertion_Sort(List):
    ''' Objective of Insertion Sort is to insert an element in a proper position of a already sorted list. A list with
        only one element is treated as a sorted list..'''
    for j in range(1, len(List)):
        element = List[j]
        i = j - 1
        while i > -1 and element < List[i]:
            List[i + 1] = List[i]
            i -= 1
        List[i + 1] = element
        print List, element
    return List

print("\tCode for 'Insertion Sort'!")
# Generate 10 random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 20, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Insertion_Sort(element_list)
print " Your Sorted list by Insertion Sort is :"
print sorted_list
