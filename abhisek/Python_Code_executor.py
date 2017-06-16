'''
 Write a Python program to execute a string containing Python code.
'''
mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
    """
exec(mycode)
exec(code)
