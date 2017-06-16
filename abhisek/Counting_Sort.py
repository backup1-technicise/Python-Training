'''
Write a Python program to sort a list of elements using the shell sort algorithm.
'''

import numpy


def Count_Sort(A, low, high, n_elements):
    '''
       Basic idea of counting sort is to determine, for each input elements X, the number of elements less or equal to
       X. This information can be used to place element directly into its correct position. For example, if there are
       17 elements less that X, then X belongs to output position 18.
    '''
    ''' Creation of Count array to store the count of no. of elements which are are less or equal for each element.
     Length of Count array is the number of elements in [low, high]'''
    Count = list()
    for i in range(0, high + 1):  # Initialization of Count array.
        Count.append(0)

    ''' Counting of common elements in A'''
    processed_element = list()
    for i in range(len(A)):
        if A[i] not in processed_element:
            processed_element.append(A[i])
            Count[A[i]] += 1
        elif A[i] in processed_element:
            Count[A[i]] += 1
    print "Count Array is"
    print Count

    ''' Counting of position for each element in output array, which will sorted array'''
    Output = list()
    Position = list()
    for i in range(len(A) + 1):   # Initialization of Output Array
        Output.append(0)
    for element in Count:    # Initialization of Position Array
        Position.append(0)

    for i in range(len(Count)):
        sum_count = 0
        if i == 0:
            sum_count = 0
            Position[i] = sum_count
        else:
            for j in range(0, i + 1):
                sum_count += Count[j]
            Position[i] = sum_count
    print "Count Array is"
    print Count
    print "Position Array is"
    print Position

    for element in A:
        if element not in Output:  # For distinct elements
            output_pos = Position[element]
            Output[output_pos] = element
        else:   # For similar elements
            output_pos = Position[element] - 1
            Output[output_pos] = element
            Position[element] -= 1
        print "Output Array is"
        print Output

    return Output[1:]

print("\tCode for 'Counting Sort'! Counting Sort assumes that each element in an array in the range of low to high "
      "such as [low, high]")
range_low = int(input("Enter lower index of range : "))
range_high = int(input("Enter higher index of range : "))
no_of_elements = int(input("Enter the number of elements to sort : "))
element_list = list(numpy.random.choice(range(range_low, range_high), no_of_elements))
print "Randomly generated numbers list: "
print element_list

sorted_list = Count_Sort(element_list, range_low, range_high, no_of_elements)
print " Your Sorted list by Counting Sort is :"
print sorted_list
