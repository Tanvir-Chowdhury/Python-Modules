import multiprocessing
import concurrent.futures
import time

t1 = time.perf_counter() 

def do_something(seconds):
    print(f"I am sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")

# single 
'''p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()'''

# Mingle

'''processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()'''

# mingle with concurrents

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,3,2,1,4]
    p = executor.map(do_something, secs)
    for result in p:
        print(result)

t2 = time.perf_counter()
print(f"finished in {round(t2-t1,2)} seconds")
