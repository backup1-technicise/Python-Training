'''
Assignment 25 :

In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set
of heuristic rules can be given as follows:

    Rule 1: If the verb ends in ee add ing (if not exception: see, flee, knee, etc.)
    Rule 2: If the verb ends in e, drop e and add ing (if not exception: whistle)
    Rule 3: If the verb ends in ie, change ie to y and add ing (if not exception: lie)
    Rule 4: For words consisting of consonant-vowel-consonant at the end, double the final letter before adding ing
    ( if not exception: shop, run, travel, sit, put)
    Rule 5: By default just add ing ( if not exception: fly, burn, sing)

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its
present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect
such simple rules to work for all cases.
'''


def make_ing_form(Input_verb):
    Output_pr_participle = ''
    Suffix_TypeI = "ee"
    Suffix_TypeII = "ie"
    Suffix_TypeIII = "e"
    if Input_verb.endswith(Suffix_TypeI):  # If the verb ends in ee add ing
        ''' About endswith(): str.endswith(suffix[, start[, end]]) is its format.
            Return True if the string ends with the specified suffix, otherwise return False.
            suffix can also be a tuple of suffixes to look for. With optional start, test beginning
            at that position. With optional end, stop comparing at that position.'''
        for i in range(len(Input_verb)):
            Output_pr_participle += Input_verb[i]
        Output_pr_participle += "ing"

    elif Input_verb.endswith(Suffix_TypeII):  # If the verb ends in ie, change ie to y and add ing
        for i in range(len(Input_verb) - 2):
            Output_pr_participle += Input_verb[i]
        Output_pr_participle += "y" + "ing"

    elif Input_verb.endswith(Suffix_TypeIII):  # If the verb ends in e, drop e and add ing
        for i in range(len(Input_verb) - 1):
            Output_pr_participle += Input_verb[i]
        Output_pr_participle += "ing"

    else:   # For last two cases
        if len(Input_verb) >= 3:
            sub_Input_verb = Input_verb[len(Input_verb) - 1 - 2:len(Input_verb) + 1]
            print sub_Input_verb
            vowels = ('a', 'e', 'i', 'o', 'u')
            flag = False  # To Check pattern "consonant-vowel-consonant" at the end of a verb
            if sub_Input_verb[0] not in vowels and sub_Input_verb[1] in vowels and sub_Input_verb[2] not in vowels:
                flag = True
            if flag:  # double the final letter before adding ing
                Output_pr_participle += Input_verb + Input_verb[len(Input_verb) - 1]
                Output_pr_participle += "ing"
            else:  # By default just add ing
                Output_pr_participle += Input_verb + "ing"
        else:
            Output_pr_participle += Input_verb + "ing"

    return Output_pr_participle

Input_verb = raw_input("Enter a verb in infinitive form to get present participle form:")
print "Input Verb: ", Input_verb
Output_pr_participle = make_ing_form(Input_verb)
print "Output present participle: ", Output_pr_participle