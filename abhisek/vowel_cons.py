'''
Assignment 4: Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''

def Check_vowel(one_length_String):
    vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if one_length_String in vowel_list:
        return True
    else:
        return False

one_length_String = raw_input("Enter your one length string = ")
print one_length_String
is_vowel = Check_vowel(one_length_String)
print "Is %c is a vowel? :" %one_length_String
print is_vowel
