'''
Write a Python program to sort a list of elements using the merge sort algorithm.
'''

import numpy
iteration = 0

def Merge(A, low, mid, high):
    print "At iteration %d, Array A is :" %iteration
    print A
    global iteration
    iteration += 1
    n1 = mid - low + 1      # Number of elements in the Left sub-array.
    n2 = high - mid         # Number of elements in the Right sub-array.
    sentinal = 32767       # Sentinal element is used as End Marker for each sub-array.

    Left = list()           # Left sub-array
    for i in range(n1):     # Store elements in Left Sub-array from given array A.
        l_element = A[low + i]
        Left.append(l_element)
    Left.append(sentinal)
    print "Left Array:", Left

    Right = list()          # Right sub-array
    for j in range(n2):     # Store elements in Right Sub-array from given array A.
        r_element = A[mid + j + 1]
        Right.append(r_element)
    Right.append(sentinal)
    print "Right Array :", Right

    i = j = 0
    for k in range(low, high + 1):  # Sort the array A by merging two sorted arrays Left and Right
        if Left[i] < Right[j]:
            A[k] = Left[i]
            i += 1
        elif Right[j] < Left[i]:
            A[k] = Right[j]
            j += 1
    del Left
    del Right
    return A


def Merge_Sort(A, low, high):
    if low < high:
        mid = (low + high) / 2
        Merge_Sort(A, low, mid)
        Merge_Sort(A, mid + 1, high)
        return Merge(A, low, mid, high)


print("\tCode for 'Merge Sort'!")
# Generate random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 20, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Merge_Sort(element_list, 0, len(element_list) - 1)
print " Your Sorted list by Merge Sort is :"
print sorted_list