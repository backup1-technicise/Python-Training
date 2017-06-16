'''
Assignment 12: Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''

def histogram(List):
    Char = "*"
    for i in List:
        for j in range(i):
            print Char,
        print '\n'

numbers = int(input(" Enter the number of elements for histogram :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = int(input())
    input_list1.append(element)
print "Your list of elements :", input_list1
histogram(input_list1)