'''
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently,
the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number
is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
'''

def check_perfect_number(number):
    divisor = list()

    for i in range(1, number/2 + 1):
        if number % i == 0:
            divisor.append(i)

    sum_of_divisor = 0

    for element in divisor:
        sum_of_divisor += element

    print "divisors are :", divisor
    if sum_of_divisor == number:
        print "%d is a perfect number" %number

    else:
        print "%d is not a perfect number" %number


number = int(input("Enter a number :"))
check_perfect_number(number)
