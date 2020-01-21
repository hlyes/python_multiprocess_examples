from multiprocessing import Process, Semaphore
import time
NB_PROCS = 23

in_sem = Semaphore(5)

out_sem = Semaphore(0)

def boat_process(i):
    print("  Boat {} waits to get inside the lock".format(i))
    in_sem.acquire()
    print("      Boat {} is inside the lock ".format(i))
    time.sleep(3)
    print("  Boat {} left the lock ".format(i))
    out_sem.release()
    pass


def canal_lock_process():
    remaining_boats = NB_PROCS
    while remaining_boats > 0:
        phasis_count = 5 if remaining_boats > 5 else remaining_boats
        print("Allowing boats {} to get in ...".format(phasis_count))
        
        for i in range(0,phasis_count):
            out_sem.acquire()


        print("... waiting for the boats to leave the lock")
        for i in range(0,phasis_count):
            in_sem.release()

        remaining_boats -= phasis_count
        print("#### {} boats remaining ####".format(remaining_boats))

    print("All the boats have finished passing through the lock")
    pass


if __name__ == "__main__":

    children = [Process(target=boat_process, args=(i,)) for i in range(0,NB_PROCS)]

    for c in children: c.start()

    canal_lock_process()

    for c in children: c.join()
    pass