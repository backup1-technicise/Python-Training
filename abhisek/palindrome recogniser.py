'''
Assignment 32 : Write a version of a palindrome recogniser that accepts a file name from the user, reads each line,
and prints the line to the screen if it is a palindrome. Note that punctuation, capitalization, and spacing are usually
ignored.
'''


def check_Plaindrome(input_String):
    new_input_String = ''
    for Char in input_String:
        if Char not in (",", "'", ".", " ", "?", "!"):   # Removal of special characters from String
            new_input_String += Char
    #print new_input_String
    List = list(new_input_String)
    for i in range(len(List)):
        if List[i].isupper():
            #print "True", List[i]
            List[i] = List[i].swapcase()
    #print List
    new_input_String = ''.join(List)
    #print new_input_String

    ''' Palindrome Checking Operation..'''
    length = len(new_input_String)
    check_flag = 0
    for i in range(0, length/2):  # Checking front to middle characters
        j = length - i - 1  # Checking back to middle characters
        char_i = new_input_String[i]
        char_j = new_input_String[j]
        if char_i != char_j:
            check_flag = 0
            break
        else:
            check_flag = 1
    if check_flag == 0:
        return False
    else:
        return True

fp = open("Palindrome.txt", "r")
for Line in fp:
    Line = Line.strip("\n")
    print "Current Line from file : ", Line
    print "Is Line %s is a Palindrome? : " % Line,
    print check_Plaindrome(Line)
