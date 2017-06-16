# Program with Shared Memory
from multiprocessing import Value, Array
import os

def child(n, a):
    n.value = 5.567
    for i in range(len(a)):
        a[i] = a[i] + 1
    print(n.value)
    print (a[:])

num = Value('d', 3.54678)
arr = Array('i', range(10))
print(num.value)
print (arr[:])
C_PID = os.fork()
if C_PID == 0:
        child_PID = os.getpid()
        print("Child process with PID=%d with parent ID=%d" %(child_PID, os.getppid()))
        child(num, arr)

elif C_PID > 0:
        os.wait()       # Waiting for all child processes
        parent_ID = os.getpid()
        print("Parent process with PID=%d with parent ID=%d" %(parent_ID, os.getppid()))
        num.value = 10.234
        for i in range(len(arr)):
            arr[i] = arr[i] + 5
        print(num.value)
        print (arr[:])
else:
        print("New process is not created")



