'''
Assignment 11 : Define a function generate_n_chars() that takes an integer n and a character c and returns a string,
n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx".
(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of
the exercise you should ignore that the problem can be solved in this manner.)
'''


def generate_n_chars(Char, n_repeat):
    output_String = ''
    for i in range(n_repeat):
        output_String += Char
    return output_String

c = raw_input(" Enter a character: ")
n = int(input(" Enter the number of repetition of c : "))
print "Output is :", generate_n_chars(c, n)
