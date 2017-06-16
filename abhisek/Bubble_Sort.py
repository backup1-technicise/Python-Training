'''
Write a Python program to sort a list of elements using the bubble sort algorithm.
'''

import numpy


def Bubble_Sort(List):
    for i in range(0, len(List)):
        for j in range(0, len(List) - i - 1):
            print j,
            if List[j] > List[j + 1]:
                temp = List[j]
                List[j] = List[j+1]
                List[j + 1] = temp
        print List, i
    return List


print("\tCode for 'Bubble Sort'!")
# Generate 10 random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 20, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Bubble_Sort(element_list)
print " Your Sorted list by Bubble Sort is :"
print sorted_list
