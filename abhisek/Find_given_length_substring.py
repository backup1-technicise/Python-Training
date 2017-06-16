import re
text = 'The quick brown fox jumps over the lazy dog.'

# find all three, four, five characters long words in a string
List3_to_5 = re.findall(r'\b\w{3,5}\b',text)
print List3_to_5

# find all words which are at least 4 characters long in a string
List_atleast_4 = re.findall(r'\b\w{4,}\b',text)
print List_atleast_4

'''
Important note about \b : \b matches a single length char which is not in \w. At beginning
of a given string \b matches with NULL char but in other case it matches with non-word char
For example:
1. r'\b\w{3}\b' produces ['The', 'fox', 'the', 'dog']
2. r'\w{3}\b' produces ['The', 'ick', 'own', 'fox', 'mps', 'ver', 'the', 'azy', 'dog']
3. r'\b\w{3}' produces ['The', 'qui', 'bro', 'fox', 'jum', 'ove', 'the', 'laz', 'dog']

\B works opposite of \b. It does not matches '' char at starting of string and it matches
word char.
For example:
r'\B\w{3}' produces ['uic', 'row', 'ump', 'ver', 'azy']
r'\B\w{3}\B produces ['uic', 'row', 'ump']
'''
