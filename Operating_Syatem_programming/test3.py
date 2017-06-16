from multiprocessing import Process, Manager
import os

manager = Manager()
d = manager.dict()
l = manager.list(range(10))

print(d)
print(l)
C_PID = os.fork()

if C_PID == 0:
        child_PID = os.getpid()
        print("Child process with PID=%d with parent ID=%d" %(child_PID, os.getppid()))
        d[1] = '1'
        d['2'] = 2
        d[0.25] = None
        l.reverse()
        print(d)
        print(l)
elif C_PID > 0:
        os.wait()       # Waiting for all child processes
        parent_ID = os.getpid()
        print("Parent process with PID=%d with parent ID=%d" %(parent_ID, os.getppid()))
        print(d)
        print(l)

else:
        print("New process is not created")