'''
Assignment 13: The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work
for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot
tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest
one.
'''

def max_in_list(List):
    max_element = List[0]
    max_index = 99999
    for i in range(1, len(List)):
        element_i = List[i]
        if element_i > max_element:
            max_element = element_i
            max_index = i
    return max_element, max_index + 1

numbers = int(input(" Enter the number of present in List :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list1.append(element)
print "Your list of elements :", input_list1
max_element, max_index = max_in_list(input_list1)
print "Maximum element %d occurs at index %d in List" % (max_element, max_index)