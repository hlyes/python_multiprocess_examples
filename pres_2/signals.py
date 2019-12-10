import os

import time
import  signal

NB_PROCS = 4

received_sigints = 0


# In this example the queues that exist are FIFO, we can also use ProritizedQueues and LIFO queues

def sigint_handler(signal, frame):
    print("Signal received", signal, )
    received_sigints+=1



if __name__ == '__main__':
    print("{} start workers ...".format(os.getpid()))
    finished_processes = [] * NB_PROCS

    signal(signal.SIGINT, sigint_handler)
    children = []



    while received_sigints < NB_PROCS:
        print("Waiting")
        time.sleep(1)

    exit(0)
