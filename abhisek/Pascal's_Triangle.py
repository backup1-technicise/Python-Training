'''
Write a Python function that that prints out the first n rows of the Pascal's triangle. Go to the editor
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

Sample Pascal's triangle :

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
Pascal's triangle

Each number is the two numbers above it added together
'''


def pascal_triangle(depth):
    List = list()
    for i in range(depth):
        if i == 0:
            sub_list = list()
            sub_list.append(1)
            List.append(sub_list)
            del sub_list

        elif i == 1:
            sub_list = list()
            sub_list.append(1)
            sub_list.append(1)
            List.append(sub_list)
            del sub_list
        else:
            sub_list = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    sub_list.append(List[i - 1][j - 1])
                else:
                    c = List[i - 1][j - 1] + List[i - 1][j]
                    sub_list.append(c)
            List.append(sub_list)
            del sub_list
        #print i, List

    print "Your Pascal's Triangle with depth = %d is : " % depth
    for i in range(len(List)):
        for j in range(len(List[i])):
            print "%d\t" %List[i][j],
        print "\n"

row = int(input("Enter the number of rows in Pascal's triangle:"))
pascal_triangle(row)
