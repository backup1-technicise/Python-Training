'''
Assignment 14 : Write a program that maps a list of words into a list of integers representing the lengths of the
corresponding words.
'''

def word_to_length(word_List):
    word_length = dict()
    for element in word_List:
        word_length[element] = len(element)
    return word_length

numbers = int(input(" Enter the number of words in List :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list1.append(element)
print "Your list of elements :", input_list1
print "Words and its corresponding lengths are : "
print word_to_length(input_list1)
