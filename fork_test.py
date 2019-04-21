import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("my PID is",os.getpid()) #子进程PID
    print("my parent process-1 PID is",os.getppid()) #父进程PID
    sleep(5)
    print("my parent process-2 PID is",os.getppid()) #父进程PID
    print("this is child process")
else:
    sleep(1)
    print("===========================")
    print("the PID is",pid) #父进程中fork()返回值　＝　子进程PID
    print("the parent PID is",os.getpid()) #父进程PID
    print("this is parent process")