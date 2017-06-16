''' Assignment 9 : Write a function is_member() that takes a value (i.e. a number, string, etc) x and
a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly
what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
'''


def Binary_Search(low, high, A, element):
    if low <= high:
        mid = (low + high) / 2
        if element == A[mid]:
            return mid
        elif element < A[mid]:
            return Binary_Search(low, mid - 1, A, element)
        else:
            return Binary_Search(mid + 1, high, A, element)
    else:
        return -1


# is_member() uses Binary Search for searching element in list
def is_member(x, List):
    List.sort()
    low_index = 0
    high_index = len(List) - 1
    val = Binary_Search(low_index, high_index, List, x)
    if val != -1:
        return True
    else:
        return False

numbers = int(input(" Enter the number of elements in a list :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list.append(element)
print "Your list of elements :", input_list
x = int(input(" Enter an element to search over a list :"))
print"Is %d in input_list ? :" % x, is_member(x, input_list)



