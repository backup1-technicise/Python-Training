'''
Write a Python program to do a case-insensitive string replacement.
'''
import re
text1 = "PHP Exercises"
text2 = "MySQL Exercises"
text3 = "Algo Exercises"

print("Original Text: ", text1)
new_text1 = re.sub(r'^[a-z|A-Z]+', r'My sem 1', text1)
print("New Text: ", new_text1)


print("Original Text: ", text2)
new_text2 = re.sub(r'^[a-z|A-Z]+', r'My sem 2', text2)
print("New Text: ", new_text2)


print("Original Text: ",text3)
new_text3 = re.sub(r'^[a-z|A-Z]+', r'My sem 3', text3)
print("New Text: ", new_text3)
