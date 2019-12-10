import os
from multiprocessing import Value, Array, Process
from random import randint
import time


NB_PROCS = 4


# In this example the queues that exist are FIFO, we can also use ProritizedQueues and LIFO queues


def pool_worker(i, finished, res):
    time.sleep(randint(0, 5))
    computed = randint(0, 1000)

    print("{} computed {}".format(os.getpid(), computed))
    res[i] = computed
    finished.value += 1


if __name__ == '__main__':
    print("{} start workers ...".format(os.getpid()))
    results_array = Array("i", range(NB_PROCS))
    finished_calculations = Value("d", 0)

    results_array
    children = []

    for i in range(NB_PROCS):
        children.append(Process(target=pool_worker, args=(i, finished_calculations, results_array)))

    for c in children:
        c.start()

    while finished_calculations.value < NB_PROCS:
        print ("Waiting")
        time.sleep(1)

    for c in children:
        c.join()
    exit(0)
