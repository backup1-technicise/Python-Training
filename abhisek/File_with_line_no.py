'''
Assignment 37 : Write a program that given a text file will create a new text file in which all the lines from
the original file are numbered from 1 to n (where n is the number of lines in the file).
'''


def Add_line_number(FP):
    modified_content_list = list()
    line_count = 1
    FP.seek(0)      # Rewind the file pointer FP at the beginning
    for element in FP:
        Modified_file_content = ''
        Modified_file_content = Modified_file_content + str(line_count) + ". " + element
        modified_content_list.append(Modified_file_content)
        del Modified_file_content
        line_count += 1
    FP.close()

    fp1 = open("New_Text_content.txt", "w")
    for new_element in modified_content_list:
        fp1.write(new_element)
    fp1.close()
    fp1 = open("New_Text_content.txt", "r")
    print "Content in file New_Text_content.txt is :", fp1.read()
    fp1.close()

fp = open("Text_content.txt", "r")
print "File's previous content : ", fp.read()
Add_line_number(fp)


