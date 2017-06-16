'''
Assignment 6 : Define a function sum() and a function multiply() that sums and multiplies (respectively) all
the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4])
should return 24.
'''

def sum(input_list):
    result = 0
    for element in input_list:
        result += element
    return result


def multiply(input_list):
    result = 1
    for element in input_list:
        result *= element
    return result


numbers = int(input(" Enter the number of elements to multiply and sum :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list.append(element)
print "Your list of elements :", input_list
Sum = sum(input_list)
Multiplication = multiply(input_list)
print "Sum is : ", Sum
print "Multiplication is : ", Multiplication
