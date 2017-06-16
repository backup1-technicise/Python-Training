'''
Write a Python program that matches a string that has an a followed by two to three 'b'.
'''
import re

'''  matches a string that has an a followed by zero or one 'b'.'''
def text_match1(str):
    match = re.search(r'(\w*ab?\w*|\w*ab?|ab?\w*)', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

''' matches a string that has an a followed by one or more b's. '''
def text_match2(str):
    match = re.search(r'(\w*ab+\w*|\w*ab+|ab+\w*)', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False


''' matches a string that has an a followed by zero or more b's'''
def text_match3(str):
    match = re.search(r'(\w*ab*\w*|\w*ab*|ab*\w*)', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

print(text_match1("ab"))
print(text_match1("abc"))
print(text_match1("abbc"))
print(text_match1("aabbc"))
print "-----------------------------------------------------------------------------------------------------------"

print(text_match2("ab"))
print(text_match2("abc"))
print "-----------------------------------------------------------------------------------------------------------"

print(text_match3("ac"))
print(text_match3("abc"))
print(text_match3("abbc"))