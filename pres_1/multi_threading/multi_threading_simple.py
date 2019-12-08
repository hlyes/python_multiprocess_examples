from threading import Thread, get_ident
import time
import os
import sys

value = 20000
with_global = False


def thread_handler(name, value_new):
    """ A simple thread handler """
    if with_global:
        """ the  keyword global must be set """
        #global value
    time.sleep(10)
    value = value_new
    print(
        "The thread {}/{} named {} says: {}".format(
            #
            get_ident(),
            os.getpid(),
            name,
            value_new,
        )
    )


if __name__ == "__main__":

    if len(sys.argv):
        with_global = True

    print("{}: value before thread run {}".format(os.getpid(), value))
    thread = Thread(target=thread_handler, args=["Thread", 2222])
    thread.start()
    for i in range(10):
        time.sleep(1)
        print("{}: value during thread run {}".format(os.getpid(), value))
    thread.join()
    print("{}: value after thread run {}".format(os.getpid(), value))
