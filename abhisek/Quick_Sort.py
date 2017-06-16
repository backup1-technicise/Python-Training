'''
Write a Python program to sort a list of elements using the quick sort algorithm.
'''

import numpy
iteration = 0

def Partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i + 1]
    A[i + 1] = pivot
    A[high] = temp
    pivot_pos = (i + 1)
    return pivot_pos


def Quick_Sort(A, low, high):
    if low < high:
        pivot_pos = Partition(A, low, high)
        Quick_Sort(A, low, pivot_pos - 1)
        Quick_Sort(A, pivot_pos + 1, high)
        #return Merge(A, low, mid, high)
        return A


print("\tCode for 'Quick Sort'!")
# Generate random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 10, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Quick_Sort(element_list, 0, len(element_list) - 1)
print " Your Sorted list by Quick Sort is :"
print sorted_list