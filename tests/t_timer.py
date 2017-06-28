import time
import sys

run = input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 2:
        print(">>>>>>>>>>>>>>>>>>>>> %f", mins)
        # Sleep for a minute
        time.sleep(10)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
    print('wake up')

# test queue and thread

from Queue import Queue
from threading import Thread

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()

q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  q.put(x)

q.join()

# simple queue class to use  a list
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
