'''
Assignment 30 : Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} and use it to translate your
Christmas cards from English into Swedish. Use the higher order function map() to write a function translate()
that takes a list of English words and returns a list of Swedish words.
'''


def translate(english_word_list):
    English_To_Swedish_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    Swedish_word_list = map(lambda Eng_word: English_To_Swedish_dict[Eng_word],  english_word_list)
    print "Your swedish words are:"
    for word in Swedish_word_list:
        print word, " ",

numbers = int(input(" Enter the number of English words :"))
input_list = list()
for i in range(1, numbers + 1):
    print "Word %d:" % i,
    Word = raw_input()
    input_list.append(Word)
print "Your list of English words :", input_list
translate(input_list)
