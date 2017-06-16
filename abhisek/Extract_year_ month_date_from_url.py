'''
Write a Python program to extract year, month and date from a url.
'''

import re
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-" \
      "little-ball-josh-norman-tells-author/"
List = re.findall(r'\d{4}/\d{2}/\d{2}', url1)
print List
