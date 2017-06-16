'''
Assignment 7 : Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
'''


def Check_prime(num):
    status = True
    for i in range(2, num - 1):
        if num % i == 0:
            print "%d is not a prime number:" % num
            status = False
            break
    if status:
        print "%d is a prime number:" % num

number = int(input("Enter a number to check Prime or Not:"))
Check_prime(number)


