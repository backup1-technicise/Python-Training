'''
Assignment 27 : Write a program that maps a list of words into a list of integers representing the lengths of the
corresponding words. Write it in three different ways:
1) using a for-loop,
2) using the higher order function map(),
and 3) using list comprehensions.
'''

def word_to_length_using_list(word_List):
    word_length = list()
    for element in word_List:
        word_length.append(len(element))
    return word_length


def word_to_length_using_map(word_List):
   '''
        In map(function, sequence), lambda function is applied over each word from word_list and returns a list
        with their corresponding length....
   '''
   word_length = map(lambda word: len(word), word_List)
   return word_length


def word_to_length_using_list_comprehension(word_List):
   word_length = [len(word) for word in word_List]
   return word_length

numbers = int(input(" Enter the number of words in List :"))
input_list1 = list()
for i in range(1, numbers + 1):
    print "Element %d:" %i,
    element = raw_input()
    input_list1.append(element)
print "Your list of elements :", input_list1

print "Words and its corresponding lengths by using list : "
print word_to_length_using_list(input_list1)

print "Words and its corresponding lengths by using map() : "
print word_to_length_using_map(input_list1)

print "Words and its corresponding lengths by using List comprehension : "
print word_to_length_using_map(input_list1)
