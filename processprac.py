# from multiprocessing import Process
# import os

# def foo():
#     print('child process', os.getpid())
    
# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child1 = Process(target=foo).start()
#     child2 = Process(target=foo).start()
#     child3 = Process(target=foo).start()
    
# def foo():
#     print('This is foo')

    
# def bar():
#     print('This is bar')
    
# def baz():
#     print('This is baz')

# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child1 = Process(target=foo).start()
#     child2 = Process(target=bar).start()
#     child3 = Process(target=baz).start()



import threading
import os
from multiprocessing import Process


def foo():
    print('process id', os.getpid())
    
if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = Process(target=foo).start()
