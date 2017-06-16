'''
Write a Python program to convert a date of yyyy-mm-dd format to to dd-mm-yyyy format.
'''

import re
dt1 = "2026-01-02"
List = re.split(r'-', dt1)
print List
temp = List[0]
List[0] = List[2]
List[2] = temp
new_date_format = '-'.join(List)
print new_date_format
print "Previous date format:", dt1
print "new_date_format:",
print re.sub(r'\d{4}-\d{2}-\d{2}', new_date_format, dt1)