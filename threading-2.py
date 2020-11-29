import threading
import time

start = time.perf_counter()

def do_something():
    print("I am sleeping for 1 sec")
    time.sleep(1)
    print("done sleeping")


t1 = threading.Thread(target=do_something) # making a thread (1)
t2 = threading.Thread(target=do_something) # making a thread (2)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')