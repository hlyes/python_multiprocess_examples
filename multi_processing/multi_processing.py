import os
from multiprocessing import Process
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
        print("Hello from process {} with pid {}".format(name, os.getpid()))


if __name__ == "__main__":
    p = Process(target=child_process, args=["Kid"])

    p.start()

    for i in range(5):
        time.sleep(1)
        print("Parent process {} says hello".format(os.getpid()))

    p.join()

    exit(0)
