'''
Assignment 7 : Define a function reverse() that computes the reversal of a string. For example,
reverse("I am testing") should return the string "gnitset ma I".
'''

def reverse(input_string):
    reversed_string = ''
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string

input_string = raw_input("Enter your string = ")
print "Given String : ", input_string
print "Reversed String : ", reverse(input_string)
