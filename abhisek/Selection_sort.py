'''
Write a Python program to sort a list of elements using the selection sort algorithm.
'''

import numpy

def Selection_Sort(List):
    for i in range(len(List) - 1):
        min_element = List[i]    # Assume first element is the lowest element
        min_index = i

        new_min_element = 9999
        new_min_index = 999
        for j in range(i + 1, len(List)):
            if List[j] < new_min_element:       # Trying to searching for min element which is not first element
                new_min_element = List[j]
                new_min_index = j
        if new_min_element < min_element:       # when first element and another min element are not same
            temp = min_element
            List[min_index] = new_min_element
            List[new_min_index] = temp
    return List


print("\tCode for 'Selection Sort'!")
# Generate 10 random element and search for an element X
element_list = list(numpy.random.choice(range(1, 500), 20, replace=False))
print "Randomly generated numbers list: "
print element_list
sorted_list = Selection_Sort(element_list)
print " Your Sorted list by Selection Sort is :"
print sorted_list
