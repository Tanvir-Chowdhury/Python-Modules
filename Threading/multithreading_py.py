from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):                  # Thread 1
            print(f"hello {i+1}")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print(f"hi {i+1}")              # Thread 2
            sleep(1)

t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()

print(active_count()) # How many threads are active?
print(current_thread()) # Which thread is active now?
print(enumerate()) # Tell us the name of all threadings. 

# Main threads waits untill the (.join) executes.
t1.join() 
t2.join()

print("bye")


print(active_count())