'''
Assignment 23 : Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two
or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the
period is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return
"This is very funny and cool. Indeed!" Tip: Use regular expressions!
'''

def correct(Input_String):
    prev_char = ''
    next_char = ''
    Output_String = ''
    Char_List = list(Input_String)
    for i in range(len(Char_List)):
        if i != 0:
            present_char = Char_List[i]
            prev_char = Char_List[i - 1]
            if prev_char == ' ' and present_char == ' ':
                continue
            elif prev_char == '.' and present_char.isalpha():
                Output_String += ' '
                Output_String += present_char
            else:
                Output_String += present_char
        else:
            present_char = Char_List[i]
            Output_String += present_char

    return Output_String

Input_String = raw_input("Enter your String to correct white spaces:")
print Input_String
Output_String = correct(Input_String)
print Output_String

