'''
Write a Python program to sort a list of elements using the shell sort algorithm.
'''

import numpy
import math


def Insertion_Sort(A, sub_List, Interval):  # It sorts the array A based on given indices under sub-list
    for i in range(1, len(sub_List)):
        index_i = sub_List[i]           # Present indices
        element = A[index_i]
        j = i - 1
        index_j = sub_List[j]           # Previous indices
        while j >= 0 and A[index_j] > element:
            index_j_increase = sub_List[j + 1]
            A[index_j_increase] = A[index_j]
            j -= 1
            index_j = sub_List[j]
        index_j = sub_List[j + 1]
        A[index_j] = element

    print A,
    print "Gap or Interval:", Interval,
    print "Sub_list or Gap", sub_List


def Shell_Sort(A, low, high, length):
    '''
        Shell sort creates a set of sub-lists of size as Interval length from A and it calls insertion
        sort on each sub-list to do the swapping operations on A to sort it in ascending order...
    '''
    Interval = 1                        # Initial value of Gap or Interval
    Interval = Interval * 3 + 1         # Starting value of Interval using Knuth Formula
    while Interval > 0:
        for i in range(low, high + 1):
            j = i
            sub_List = list()
            while j <= high:
                sub_List.append(j)      # Creation of Shell or Sub lists
                j += Interval
            Insertion_Sort(A, sub_List, Interval)  # Insertion sort is called for each sub-list
            del sub_List
        Interval /= 2

    return A

print("\tCode for 'Shell Sort'!")
# Generate random elements and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 20, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Shell_Sort(element_list, 0, len(element_list) - 1, len(element_list))
print " Your Sorted list by Shell Sort is :"
print sorted_list
