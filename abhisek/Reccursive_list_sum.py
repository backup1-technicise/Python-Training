''' Write a Python program of recursion list sum
'''

def rec_list_sum(List, list_len):
    if list_len == 1:
        if type(List[0]) == type(list()):
            sum_list = 0
            for element in List[0]:
                sum_list += element
            return sum_list
        else:
            return List[0]
    else:
        if type(List[0]) == type(list()):
            return rec_list_sum(List[0], len(List[0])) + rec_list_sum(List[1:], len(List[1:]))
        else:
            return List[0] + rec_list_sum(List[1:], len(List[1:]))

given_list = [[3,4],[5,6], 1, 2]

list_sum = rec_list_sum(given_list, len(given_list))

print "Result of recurrsive list sum : %d" %list_sum