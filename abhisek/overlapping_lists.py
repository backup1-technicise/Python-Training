'''
Assignment 10 : Define a function overlapping() that takes two lists and returns True if they have at least one member
in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
'''
count_is_member = 0  # Counts no. of execution of is_member()


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


def is_member(x, List):  # is_member() uses Binary Search for searching element in list
    if count_is_member == 0:
        List.sort()
        low_index = 0
        high_index = len(List) - 1
        val = Binary_Search(low_index, high_index, List, x)
    else:
        low_index = 0
        high_index = len(List) - 1
        val = Binary_Search(low_index, high_index, List, x)

    global count_is_member
    count_is_member += 1

    if val != -1:
        return True
    else:
        return False


def overlapping(List1, List2):
    flag = 0
    for item in List1:
        common = is_member(item, List2)
        if common:
            flag = 1
            break
        elif not common:
            continue
    if flag == 1:
        return True
    else:
        return False

numbers_1 = int(input(" Enter the number of elements in list 1 :"))
input_list1 = list()
for i in range(1, numbers_1 + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list1.append(element)
print "Your list of elements :", input_list1

numbers_2 = int(input(" Enter the number of elements in list 2 :"))
input_list2 = list()
for i in range(1, numbers_2 + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list2.append(element)
print "Your list of elements :", input_list2

print " Is there any common elements between two lists ? :", overlapping(input_list1, input_list2)