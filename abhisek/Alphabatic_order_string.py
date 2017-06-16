'''
Write a Python program that accepts a hyphen separated sequence of words as input and prints the words in a
hyphen-separated sequence after sorting them alphabetically. Go to the editor

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

'''


def alphabetic_sequence(Sample_Items):
    Sample_Items_list = Sample_Items.split("-")
    Sample_Items_list.sort()
    Expected_result = '-'.join(Sample_Items_list)
    print "Expected_result :",
    print Expected_result


Sample_Items = "green-red-yellow-black-white"
print "Sample_Items : green-red-yellow-black-white"
alphabetic_sequence(Sample_Items)
