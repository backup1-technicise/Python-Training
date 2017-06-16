'''Write a Python program to converting an integer to a string in 16 base.'''


def Deci_to_Hex(number):
    if number < 16:
        if number in range(0, 10):
            return str(number)
        else:
            return Hex_system[number]
    else:
        rem = number % 16
        number /= 16
        return Deci_to_Hex(number) + str(rem)


Hex_system = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}    # 0-9 are fine
Decimal_number = int(input("Enter the decimal number:"))
result = Deci_to_Hex(Decimal_number)
print result

