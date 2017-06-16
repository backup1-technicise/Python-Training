'''
Assignment 2: Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''

def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

number1 = int(input("Enter first number = "))
number2 = int(input("Enter second number = "))
number3 = int(input("Enter third number = "))
largest = max_of_three(number1, number2, number3)
print "The largest number among 3 nos. is : %d" %largest