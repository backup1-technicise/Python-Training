'''
Write a Python program to remove leading zeros from an IP address.
'''

import re
ip = "216.08.094.196"
splitted_list = re.split(r'\.', ip)
print splitted_list
for i in range(len(splitted_list)):
    string = splitted_list[i]
    match = re.search(r'\b0{1}\d+', string)
    if match:
        splitted_list[i] = string.lstrip('0')
print splitted_list
new_IP = '.'.join(splitted_list)
print new_IP
