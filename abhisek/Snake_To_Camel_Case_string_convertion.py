'''
Write a python program to convert snake case string to camel case string.

Snake case (or snake_case) is the practice of writing compound words or phrases in which the elements are
separated with one underscore character (_) and no spaces, with each element's initial letter usually lower cased
within the compound and the first letter either upper or lower case as in "foo_bar" and "Hello_world". It is commonly
used in computer code for variable names, and function names, and sometimes computer file names.

Camel case (also camelCase, CamelCase, camel caps or medial capitals) is the practice of writing compound words or
phrases such that in each word or abbreviation in the middle of the phrase begins with a capital letter, with no spaces
or hyphens. Camel case may start with a capital letter or with a lowercase letter. Common examples include:
"HarperCollins", "iPhone" and "FedEx". It is also sometimes used in online usernames such as "JohnSmith", and to make
multi-word domain names more legible e.g. in advertisements.

CamelCase is named after the "humps" of its capital letters
'''


import re
snake_case_1 = "foo_bar"
snake_case_2 = "Hello_world"
snake_case_3 = "John_smith"
snake_case_4 = "Harper_collins"
snake_case_5 = "Fed_ex"

List = re.split(r'_', snake_case_1)
CamelCase1 = ''
for word in List:
    CamelCase1 += word.capitalize()
print "Snake case:", snake_case_1
print "Camale case:", CamelCase1
del List

List = re.split(r'_', snake_case_2)
CamelCase2 = ''
for word in List:
    CamelCase2 += word.capitalize()
    
print "Snake case:", snake_case_2
print "Camale case:", CamelCase2
del List

List = re.split(r'_', snake_case_3)
CamelCase3 = ''
for word in List:
    CamelCase3 += word.capitalize()
print "Snake case:", snake_case_3
print "Camale case:", CamelCase3
del List

List = re.split(r'_', snake_case_4)
CamelCase4 = ''
for word in List:
    CamelCase4 += word.capitalize()
print "Snake case:", snake_case_4
print "Camale case:", CamelCase4
del List

List = re.split(r'_', snake_case_5)
CamelCase5 = ''
for word in List:
    CamelCase5 += word.capitalize()
print "Snake case:", snake_case_5
print "Camale case:", CamelCase5
del List
