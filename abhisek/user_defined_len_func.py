'''
Assignment 3: Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing
it yourself is nevertheless a good exercise.)
'''

def len(given_String):
    count_char = 0
    for char in given_String:
        count_char += 1
    return count_char

given_string = raw_input("Enter your string = ")
print given_string
nchar = len(given_string)
print "Number of charecters in a given string is : %d" %nchar
