import os
from multiprocessing import Process, cpu_count
import signal
import time

"""
A simple way to create a process  and run it by passing arguments to it
"""


def child_process(name):
    """
    A function that is called by the process when it is launched
    """
    for i in range(5):
        time.sleep(1)
        print("{} with pid {} ---- {}".format(name, os.getpid(), i))


if __name__ == "__main__":
    
    processes = [
        Process(target=child_process, args=["Kid #{}".format(i)])
        for i in range(cpu_count())
    ]

    for p in processes:
        p.start()

    for i in range(3):
        time.sleep(1)
        print("Parent process {} says hello".format(os.getpid()))

    
    for p in processes:
        p.terminate()
        # Does the same as:
        # os.kill(p.pid, signal.SIGTERM)

    # In case we
    # for p in processes:
    #     p.join()

    print("End of father")

    exit(0)
