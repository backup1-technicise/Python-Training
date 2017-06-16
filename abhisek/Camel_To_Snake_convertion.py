import re
CamelCases = ["HelloWorld", "FooBar", "JohnSmith", "HarperCollins", "FedEx"]

for CamelCase in CamelCases:
    snake_case = ''
    List = re.findall(r'[A-Z]{1}[a-z]+',CamelCase)  # create list from Camel case word..
    for i in range(len(List)):
        if i == len(List) - 1:
            match = re.search(r'(^[A-Z]{1})([a-z]+)', List[i])
            if match.group(1):
                snake_case += re.sub(r'^[A-Z]{1}','_'+match.group(1).lower(),List[i])  # Apply rules for
                                                                                       # snake word
        else:
            snake_case += List[i]
    print "Camel case word", CamelCase
    print "Snake case word:", snake_case
    del List
