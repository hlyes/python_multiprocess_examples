import os
from multiprocessing import Process
import time

"""
A simple way to create a process  and run it by passing arguments to it
"""


class ChildProcess(Process):
    def __init__(self, name, *args, **kwargs):
        super(ChildProcess, self).__init__()
        self.name = name

    def run(self):
        """
        A function that is called by the process when it is launched
        """
        for i in range(5):
            time.sleep(1)
            print("Hello from process {} with pid {}".format(self.name, self.pid))
        

if __name__ == "__main__":
    p = ChildProcess("Kid")

    p.start()

    for i in range(5):
        time.sleep(1)
        print("Parent process {} says hello".format(os.getpid()))

    p.join()

    exit(0)
