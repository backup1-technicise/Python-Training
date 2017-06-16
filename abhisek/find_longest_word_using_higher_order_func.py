'''
Assignment 28: Write a function find_longest_word() that takes a list of words and returns the length of the longest
one. Use only higher order functions.
'''


def find_longest_word(word_List):
    '''
         Here I use three higher order functions such as map(), reduce() and filter() to find maximum length Strings
    '''
    length_list = map(lambda word: len(word), word_List)  # map() maps String lengths in a list
    max_length = reduce(lambda length_1, length_2: length_1 if length_1 > length_2 else length_2, length_list)  # reduce() reduces length list to find maximum String length
    max_length_string = filter(lambda word: len(word) == max_length, word_List) # filter() filter outs strings with maximum length.
    return max_length_string, max_length

numbers = int(input(" Enter the number of words in List :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list.append(element)
print "Your list of elements :", input_list

max_length_string, max_length = find_longest_word(input_list)
print "Strings ", max_length_string,
print " with maximum length %d" % max_length

