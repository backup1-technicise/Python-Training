from multiprocessing import Process

def say_hello(name='world'):
    print("Hello, %s" % name)

p = Process(target=say_hello)
p.start()
p.join()