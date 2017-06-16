'''
Python: Where a string will start with a specific number
'''

import re
string_list = ['5-2345861', '6-2345861']
for string in string_list:
    match = re.search(r'^5-{1,}\d+', string)
    if match:
        print match.group(), 'True'
    else:
        print string, 'False'
