import threading
import concurrent.futures
import time

start = time.perf_counter()

def do_something(second):
    print(f"I am sleeping for {second} second(s)")
    time.sleep(second)
    return "done sleeping"


t1 = threading.Thread(target=do_something) # making a thread (1)
t2 = threading.Thread(target=do_something) # making a thread (2)

t1.start()
t2.start()

t1.join()
t2.join() 

# making 10 threads

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# alternative of threading

with concurrent.futures.ThreadPoolExecutor() as executor:
    
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())

    secs = [5,4,3,2,1,1,4,3,2,5]

    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# alternative of threading and concurrent.submit

with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5,5,4,3,2,1,4,3]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')