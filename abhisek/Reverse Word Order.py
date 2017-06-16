'''
Assignment 2: Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.

For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

given_string = "My name is Michele"
string_list = given_string.split(" ")
string_list.reverse()
output_string = " ".join(string_list)
print "Given String :", given_string
print "Output String : ", output_string