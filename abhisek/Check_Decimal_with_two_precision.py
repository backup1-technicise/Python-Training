''' Write a Python program to check a decimal with a precision of 2.
'''

def is_decimal(num):
    import re
    match = re.search(r'^([0-9]+)\.([0-9]{1,2})?$', num)  # It is equivalent to r'^(\d+)\.(\d{1,2})?'

    if match:
        print match.group(1)    # Before '.' operator
        print match.group(2)    # After '.' operator
        print match.group(),    # Given number after pattern matching
        print "is a decimal number with 2 precision"
    else:
        print num,
        print "is not a decimal number with 2 precision"


is_decimal('123.11')
is_decimal('123.1')
is_decimal('123')
is_decimal('0.21')

is_decimal('123.1214')
is_decimal('3.124587')
is_decimal('e666.86')
