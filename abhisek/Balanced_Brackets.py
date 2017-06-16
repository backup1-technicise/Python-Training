'''
Assignment 46 :  Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/
    closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK


'''
def isEmpty(STACK):
    if len(STACK) == 0:
        return True


def parChecker(symbolString):
    stack = list()              # Stack Data structure
    balanced = True             # Check for balanced parentheses
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "[":
            stack.append(symbol)        # For open bracket '[' PUSH it
        else:
            if isEmpty(stack):
                balanced = False        # if no matching ']' for ']'
            else:
                stack.pop()             # Else POP ']' for '['

        index += 1

    if balanced and isEmpty(stack):     # Nothing to POP and balanced flag is true
        return "OK"
    else:
        return "Not OK"

print("[]", parChecker('[]'))
print("[][]", parChecker('[][]'))
print("[[][]]", parChecker('[[][]]'))
print("][", parChecker(']['))
print("][][", parChecker('][]['))
print("[]][[]", parChecker('[]][[]'))