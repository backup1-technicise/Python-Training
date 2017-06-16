'''
Assignment 42 : A sentence splitter is a program capable of splitting a text into sentences. The standard set of
heuristics for sentence splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "." (periods), "?" or "!", except that

    A. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
    B. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
    C. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are
       not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    D. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
       (for example, www.aptex.com, or e.g).
    E. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence
       boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each sentence
on a separate line.
Test your program with the following short text:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.

The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.

'''


def Period_rules(Char, ip_string, Char_index):
    status = False  # Test whether '.' produces a sentence or not.
    Char_prev = ip_string[Char_index - 1]
    Char_next = ip_string[Char_index + 1]

    sample_title_list = ["Mr.", "Mrs.", "Dr.", "Jr."]
    punctuation_list = [",", "."]

    if Char_next == ' ' and ip_string[Char_index + 2].isalpha() and ip_string[Char_index + 2].islower():  # Rule A
        status = True

    if Char_next != ' ' and Char_next.isdigit():  # Rule B
        status = True

    if Char_next == ' ' and ip_string[Char_index + 2].isalpha() and ip_string[Char_index + 2].isupper():  # Rule C
        sample_title = ip_string[Char_index - 2] + Char_prev + Char
        print sample_title
        if sample_title in sample_title_list:
            status = True

    if Char_next != ' ' and Char_next.isalpha() and Char_next.islower():  # Rule D
        status = True

    if Char_next in punctuation_list:   # Rule E
        status = True

    return status


def sentence_Splitter(input_string):
    output_string = ''
    for i in range(len(input_string)):
        Char = input_string[i]
        if Char not in ('.', '?', '!'):
            output_string += Char
        else:
            if Char == '.' and i == len(input_string) - 1:  # Last Char in input string is '.' no rule.
                                                            # Just add '.' as terminator.
                output_string += Char

            if Char == '.' and i != len(input_string) - 1:   # '.' is not as last character. So, apply rules
                status = Period_rules(Char, input_string, i)  # if status is "True" not sentence boundary,
                                                                # else sentence boundary.
                if status:
                    output_string += Char
                else:
                    output_string += Char
                    output_string += '\n'

            if Char == '!':
                output_string += Char
                output_string += '\n'

            if Char == '?':
                output_string += Char
                output_string += '\n'

    return output_string

fp = open("Sentence_Splitter.txt", "r")
input_string = fp.read()
print "File's present content : ", input_string
output_string = sentence_Splitter(input_string)

print output_string
print len(output_string)

output_string_list = list(output_string)
print output_string_list
print len(output_string_list)

output_string = ''  # Modify output string by removing ' ' @ begin of a line
for i in range(len(output_string_list)):
    print i, output_string_list[i]
    if output_string_list[i] == ' ' and output_string_list[i - 1] == '\n':  # Remove ' ' @ begin of a line
        continue
    else:
        output_string += output_string_list[i]

print "Sentences from File's present content \n: ", output_string
fp.close()
fp = open("Sentence_Splitter.txt", "a")  # Append sentences as Output with Input String
fp.write("\n\n\n")
fp.write(output_string)
