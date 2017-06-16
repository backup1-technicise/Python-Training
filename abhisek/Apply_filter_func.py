'''
Assignment 29 : Using the higher order function filter(), define a function filter_long_words() that takes a list of
words and an integer n and returns the list of words that are longer than n.
'''


def filter_long_words(input_list, n):
    Filtered_word = filter(lambda word: len(word) > n, input_list) # filter() filter outs strings with maximum length.
    return Filtered_word

numbers = int(input(" Enter the number of words in List :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list.append(element)
print "Your list of elements :", input_list

n = int(input(" Enter the value of n :"))  # See the details of n in problem statement.

Word_list = filter_long_words(input_list, n)
print "List of words", Word_list,
print "with length > %d" % n