''' Assignment 8 : Define a function is_palindrome() that recognizes palindromes
(i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True. '''

def is_Palindrome(input_string):
    length = len(input_string)
    check_flag = 0
    for i in range(0, length/2):  # Checking front to middle characters
        j = length - i - 1  # Checking back to middle characters
        char_i = input_string[i]
        char_j = input_string[j]
        if char_i != char_j:
            check_flag = 0
            break
        else:
            check_flag = 1
    if check_flag == 0:
        return False
    else:
        return True

input_string = raw_input("Enter your string = ")
print "Given String : ", input_string
print "Is String %s is a Palindrome? : " % input_string,
print is_Palindrome(input_string)
