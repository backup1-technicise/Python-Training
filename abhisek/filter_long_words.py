'''
Assignment 16 ; Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.
'''


def filter_long_words(word_List, length):
    word_length = dict()
    for element in word_List:
        word_length[element] = len(element)
    output_list = list()
    for key, value in word_length.iteritems():
        if value > length:
            output_list.append(key)

    return output_list

numbers = int(input(" Enter the number of words in List :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list1.append(element)
print "Your list of elements :", input_list1
length = int(input("Enter the length of words to search:"))
word_list = filter_long_words(input_list1, length)
print "A list of words of length %d are as follows:" %length
print word_list
