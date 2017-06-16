'''
Assignment 1: Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers
up to 1000.
'''

List_Prime_numbers = list()
List_happy_numbers = list()
fp_prime = open("primenumbers.txt", "r")
fp_happy = open("happynumbers.txt", "r")

for prime_number in fp_prime:
    prime_number = prime_number.strip('\n')
    List_Prime_numbers.append(int(prime_number))

for happy_number in fp_happy:
    happy_number = happy_number.strip('\n')
    List_happy_numbers.append(int(happy_number))

common_element_list = [element for element in List_Prime_numbers if element in List_happy_numbers]
print "Common element list :"
print common_element_list
