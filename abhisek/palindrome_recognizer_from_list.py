'''
Assignment 17 : Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?",
"Step on no pets",
"Sit on a potato pan, Otis",
"Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori",
"Rise to vote sir",
 or the exclamation  "Dammit, I'm mad!". '''
#                          Note that punctuation, capitalization, and spacing are usually ignored.


def check_Plaindrome(input_String):
    new_input_String = ''
    for Char in input_String:
        if Char not in (",", "'", ".", " ", "?", "!"):   # Removal of special characters from String
            new_input_String += Char
    print new_input_String
    List = list(new_input_String)
    for i in range(len(List)):
        if List[i].isupper():
            print "True", List[i]
            List[i] = List[i].swapcase()
    print List
    new_input_String = ''.join(List)
    print new_input_String

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

Str = raw_input("Enter a String for palindrome checking: ")
print "Given String : ", Str
print "Is String %s is a Palindrome? : " % Str,
print check_Plaindrome(Str)
