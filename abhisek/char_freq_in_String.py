'''
Assignment 21 : Write a function char_freq() that takes a string and builds a frequency listing of the characters
contained in it. Represent the frequency listing as a Python dictionary. Try it with something like
char_freq("abbabcbdbabdbdbabababcbcbab").
'''

def char_freq(input_String):
    counted_Char = list()
    Char_count = dict()
    for i in range(len(input_String) - 1):
        if input_String[i] not in counted_Char:
            counted_Char.append(input_String[i])
            Counter = 1
            for j in range(i + 1, len(input_String)):
                if input_String[i] == input_String[j]:
                    Counter +=1
            Char_count[input_String[i]] = Counter
    print "Occurrences of characters in given String is: "
    print Char_count

input_String = raw_input("Enter a String: ")
char_freq(input_String)