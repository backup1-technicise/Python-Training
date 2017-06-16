'''
Assignment 5: Write a function translate() that will translate a text into other string.
That is, double every consonant and place an occurrence of "o" in between. For example,
translate("this is fun") should return the string "tothohisos isos fofunon".
'''

def char_Change(given_string):
    vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    new_String = ''
    for char in given_string:
        if char not in vowel_list and char != ' ':
            temp_string = char + "o" + char  # temp_string is based on " double every consonant and place an occurrence
                                                # of "o" in between"
            new_String += temp_string
        else:
            new_String += char
    return new_String

given_string = raw_input("Enter your string = ")
new_String = char_Change(given_string)
print "Old String: ", given_string
print "Modified String: ", new_String
