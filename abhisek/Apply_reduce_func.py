'''
Assignment 26 : Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers
and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the
reduce() function directly?
'''


def max_in_list(List):
    max_element = List[0]
    max_index = 99999
    for i in range(1, len(List)):
        element_i = List[i]
        if element_i > max_element:
            max_element = element_i

    return max_element


numbers = int(input(" Enter the number of present in List :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list.append(element)
print "Your list of elements :", input_list

max_element = max_in_list(input_list)
print "%d is the Maximum element in input List" % max_element

'''  Maximum element identification using reduce() method  '''

''' Usage of reduce() method to find largest number from a list. Prototype of reduce() is as follows:
    element = reduce(function, sequence). Here, function is one-line lambda function and it is applied
    over a list of elements, called sequence...
'''
max_element = reduce(lambda a, b: a if a > b else b, input_list)  # reduce() recursively uses lambda function with
                                                                  # dual arguments.
print "%d is the Maximum element in input List" % max_element
