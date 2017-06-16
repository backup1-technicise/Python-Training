# orphan process
import os
from multiprocessing import Process
import time
def child(a, b):
    self_ID = os.getpid()
    parent_id = os.getppid()
    sum = a + b
    print("result:%d, child ID:%d, parent ID = %d" %(sum, self_ID,parent_id))

def parent(c, d):
    self_ID = os.getpid()
    parent_id = os.getppid()
    sub = c - d
    print("result:%d, parent ID:%d, parent ID = %d" %(sub, self_ID,parent_id))

val1 = 200
val2 = 100
p = Process(target=child, args=(val1, val2))
#os.wait()
#time.sleep(5)
os._exit(0)
parent(val1, val2)
p.start()
