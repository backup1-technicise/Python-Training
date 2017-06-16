'''
Write a Python program that matches a string that has an a followed by two to three 'b'.
'''
import re


def text_match(str):
    match = re.search(r'(\w*ab{2,3}\w*|\w*ab{2,3}|ab{2,3}\w*)', str)
    if match:
        print "string is:", match.group()
        return True
    else:
        print "Match is not found"
        return False

print(text_match("ab"))
print(text_match("aabbbbbc"))