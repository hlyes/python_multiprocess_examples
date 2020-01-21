import os
from multiprocessing import Queue, Process
from random import randint
import time

NB_PROCS = 4

# In this example the queues that exist are FIFO, we can also use ProritizedQueues and LIFO queues



def pool_worker(q):
    time.sleep(randint(1, 5))
    computed = randint(0, 1000)
    print("{} computed {}".format(os.getpid(), computed))
    q.put((computed, os.getpid()))



if __name__ == '__main__':
    print("{} start workers ...".format(os.getpid()))
    queue = Queue()

    children = []

    for i in range(NB_PROCS):
        children.append(Process(target=pool_worker, args=(queue,)))

    for c in children:
        c.start()
    
    for i in range(NB_PROCS):
        data = queue.get(block=True)
        print("{} received {}".format(os.getpid(), data))


    queue.close()

    for c in children:
        c.join()

    exit(0)
