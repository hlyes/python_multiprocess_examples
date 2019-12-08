import os
from multiprocessing import Pool, cpu_count
import signal
import random
import time

"""
A simple way to create a process  and run it by passing arguments to it
"""
random.seed(98902840938)


def handler(name):
    """
    A function that is called by the process when it is launched
    """
    rand = random.randint(1, 10)
    print("Process {} will sleep {} times".format(name, rand))
    for i in range(rand):
        time.sleep(1)
        print("{} with pid {} ---- {}".format(name, os.getpid(), i))
    print("============> {} finished its treatment".format(name))


def handler_multi_params(name, age):
    """
    A function that is called by the process when it is launched
    """
    rand = random.randint(1, 10)
    print("Process {} will sleep {} times".format(name, rand))
    for i in range(rand):
        time.sleep(1)
        print("{} {} with pid {} ---- {}".format(name, age, os.getpid(), i))
    print("============> {}{} finished its treatment".format(name, age))


if __name__ == "__main__":
    
    p = Pool(processes=4)

    # p.map(handler,[ "Kid #{}".format(i) for i in range(cpu_count())])
    p.starmap(
        handler_multi_params,
        [("Kid #{}".format(i), random.randint(1, i + 10)) for i in range(cpu_count())],
    )

    p.close()
    print("Pool closed")
    p.join()
    print("Join Pool")
    exit(0)
