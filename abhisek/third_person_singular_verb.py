'''
Assignment 24 :

The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the
infinitive form: run -> runs. A simple set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s

Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns
its third person singular form. Test your function with words like try, brush, run and fix. Note however that the
rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out
the string method endswith().
'''


def make_3sg_form(Input_verb):
    Output_verb = ''
    Suffix_TypeI = "y"
    Suffix_TypeII = ("o", "ch", "s", "x", "z", "sh")
    if Input_verb.endswith(Suffix_TypeI):
        ''' About endswith(): str.endswith(suffix[, start[, end]]) is its format.
            Return True if the string ends with the specified suffix, otherwise return False.
            suffix can also be a tuple of suffixes to look for. With optional start, test beginning
            at that position. With optional end, stop comparing at that position.'''
        for i in range(len(Input_verb) - 1):
            Output_verb += Input_verb[i]
        Output_verb += "ies"
    elif Input_verb.endswith(Suffix_TypeII):
        Output_verb += Input_verb + "es"
    else:
        Output_verb += Input_verb + "s"
    return Output_verb

Input_verb = raw_input("Enter a verb in infinitive form to get third person singular form:")
print "Input Verb: ", Input_verb
Output_verb = make_3sg_form(Input_verb)
print "Output Verb: ", Output_verb

