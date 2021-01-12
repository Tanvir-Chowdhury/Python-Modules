import threading
import time

def fire():
    print('firing event ....')
    event.set()

def listen():
    event.wait()
    print("event fired.")

event=threading.Event()

threads1 = []
threads2 = []

for _ in range(10):
    thread1 = threading.Thread(target=fire)
    thread2 = threading.Thread(target=listen)
    thread1.start()
    threads1.append(thread1)
    thread2.start()
    threads2.append(thread2)

for thread in threads1:
    thread.join()

for thread in threads2:
    thread.join()