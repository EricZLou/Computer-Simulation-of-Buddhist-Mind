import time
from threading import Thread
import sys
from process.queue import TQueue
from worldly.scenario import Scenario
from senses.being import Being
from senses.sense_base import *
from tests.t_scenario import get_scen


# create a dummy person/being
eye = SenseEye([10, 10])
ear = SenseEar([10, 10])
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
citta0 = None # initial citta
dummy = Being(eye, ear, nose, tongue, body, citta0)

# test queue and thread

from queue import deque

# a being runs a main thread and five sense threads
# each sense thread posts events to the TQueue
# the main thread handles the event

q = TQueue()
scen = get_scen()

def do_eye(q, scen):
    cnt = 0
    while True:
        scen.post(q)
        cnt += 1
        print('\nEvent posted...%d', cnt)
        time.sleep(10)

t_eye = Thread(target=do_eye, args=(q, scen))
t_eye.setDaemon(True)
t_eye.start()

# test one thread for eye
cnt = 0
while True:
    if q.isempty():
        time.sleep(10)
        print('\nCentral queue empty')
    else:
        cnt += 1
        e = q.get()
        rslt = dummy.process(e, e.ticks_passed)
        print('\nOne event processed...%d', cnt)
        if rslt == False:
            print('Exception... break')
            break

t_eye.join()
print('\nAll done...')

def do_man(q, being):
    while True:
        e = q.get()
        being.process(e)

# t_man = Thread(target=do_man, args=(q,))
# t_man.setDaemon(True)
# t_man.start()
# t_man.join()

def testTimer():
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

