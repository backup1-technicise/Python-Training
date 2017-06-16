'''
Assignment 15 : Write a function find_longest_word() that takes a list of words and returns the length of the longest
                one.
'''


def find_longest_word(word_List):
    word_length = dict()
    for element in word_List:
        word_length[element] = len(element)
    max_key = ''
    max_value = -9999
    for key, value in word_length.iteritems():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key, max_value

numbers = int(input(" Enter the number of words in List :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list1.append(element)
print "Your list of elements :", input_list1
key, value = find_longest_word(input_list1)
print "The largest word = %s with length = %d. " % (key, value)

