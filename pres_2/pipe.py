import os
from multiprocessing import Pipe, Process
from random import randint
import time
from select import select

NB_PROCS = 4


def pool_worker(conn):
    time.sleep(randint(0, 5))
    computed = randint(0, 1000)

    data = conn.recv()
    print("######")
    print("    {} received {} from parent".format(os.getpid(), data))
    print("    {} computed {}".format(os.getpid(), computed))
    conn.send([computed])


if __name__ == '__main__':
    print("{} start workers ...".format(os.getpid()))

    children = []
    parent_connections = []
    children_connections = []
    for i in range(NB_PROCS):
        parent, child = Pipe()
        parent_connections.append(parent)
        children_connections.append(child)
        children.append(Process(target=pool_worker, args=(child,)))

    for c in children:
        c.start()

    for c in parent_connections:
        c.send(randint(0, 2000))

    received = 0
    while received < NB_PROCS:
        print(":::::", received)
        streams = select([], parent_connections, [])

        ready_to_read = streams[1]

        for r in ready_to_read:
            try:
                data = r.recv()
                print("Parent process {} received {}".format(os.getpid(), data))
                received += 1
            except EOFError:
                continue

    for c in range(NB_PROCS):
        children_connections[c].close()
        children[c].join()

    exit(0)
