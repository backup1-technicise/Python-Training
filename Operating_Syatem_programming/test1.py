import os

print("All Environmental variables", os.environ)
print("Details of only PATH variable", os.environ['PATH'])
print("Current working directory", os.getcwd())
print("Change of directory")
os.chdir("/home/abhisekroy/PycharmProjects/")
os.chdir('/home/abhisekroy/PycharmProjects/PythonOSprocess')
print(os.getcwd())
print("Group ID connected with present process",  os.getgid())
print("User ID connected with present porcess", os.getuid())
print("List of group IDS", os.getgroups())
print("Get present process ID", os.getpid())
print("Get parent process ID", os.getppid())
#os.setgid(20)
#os.setuid(32)
#print("Group ID connected with present process",  os.getgid())
#print("User ID connected with present porcess", os.getuid())
print("execution of system call ps", os.system("ps"))
print("execution of system call ls -l", os.system("ls -l"))
