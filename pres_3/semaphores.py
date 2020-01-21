from multiprocessing import Process, Semaphore, Array

NB_PROCS
boats_in_lock = Array("i",[-1]*NB_PROCS)
in_sem = Semaphore(0)
out_sem = Semaphore(0)

def boat_process(i):
    print("Boat {} waits to get inside the lock")
    in_sem.acquire()
    print("Boat {} waits for other boats to get into the lock ")
    # something about bareer
    print("Boat {} left the lock ")
    out_sem.release()
    pass


def canal_lock_process():

    while True:
        while boats_in_lock
    pass


if __name__ == "__main__":
    
    pass