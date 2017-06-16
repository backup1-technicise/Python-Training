'''
Assignment 34 : Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen.
'''


def char_freq_table(input_String):
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
    for Char in sorted(Char_count):
        print "%c: %d" % (Char, Char_count[Char])


fp = open("Charecter_freq.txt", "r")
for Line in fp:
    Line = Line.strip('\n')
    print "Current line from file : ", Line
    char_freq_table(Line)
