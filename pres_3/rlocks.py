from multiprocessing import Process, RLock
from random import randint

def process_handler(p, lines_to_print, file_to_write, lock):
    
    if USE_LOCK:
        lock.acquire()    

    space = ' ' * p
    print("{} Child {} has to write {} lines".format(space, p, lines_to_print))
    
    for i in range(0, lines_to_print):
        
        
        str_to_write="{} Child{} prints its line number {}".format(space, p, lines_to_print)
        file_to_write.write(str_to_write)
        file_to_write.flush()
        
        file_to_write.write("\r\n")
        file_to_write.flush()
    
    print('{} Child {} leaves'.format(space,p))

    if USE_LOCK:
        lock.release()

    
    exit(0)


NB_CHILDREN = 5

USE_LOCK = True

if __name__ == "__main__":
    lock = RLock()
    file_to_write = open(file="out.txt", mode="w+")
    children = [Process(target=process_handler, args=(i,randint(0,300), file_to_write, lock)) for i in range(0,5)]
    
    for c in children:
        c.start()
    
    for c in children:
        c.join()

    print("Parent process closes file before leaving ")    
    file_to_write.close()
    print("Parent process leaves ")
    exit(0)