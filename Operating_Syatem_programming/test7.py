#Orphan process
import os
def child():
    print("in child:", os.getpid())
#	print(os.getpid())
    print("Its parent ID:", os.getppid())
#	os._exit(0)

def parent():
    newpid = os.fork()
    if newpid == 0:
        child()
    print("in parent::", os.getpid())
    os._exit(0)
#	print os.getpid()

parent()
#print os.getppid()