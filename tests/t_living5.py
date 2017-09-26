import time
from threading import Thread
import sys
from process.queue import TQueue
from process.mind import Mind
from worldly.scenario import Scenario
from senses.being import Being
from senses.sense_base import *
from tests.t_scenario import get_scen5


# create a dummy person/being
eye = SenseEye([10, 10])
ear = SenseEar([10, 10])
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
citta0 = None # initial citta
scen = get_scen5()
dummy = Being(eye, ear, nose, tongue, body, citta0)
dummy.bindScenario(scen)

# test queue and thread

from queue import deque

# a being runs a main thread and five sense threads
# each sense thread posts events to the TQueue
# the main thread handles the event

q = TQueue()  # central queue
mind = Mind(dummy)

# five door process
def do_door(q, scen):
    cnt = 0
    while True:
        scen.post(q)
        cnt += 1
        print('\nEvent posted...', cnt)
        time.sleep(10)

# mind door process
def do_mind(q, mind):
    cnt = 0
    while True:
        mind.post(q)
        cnt += 1
        print('\nMind event posted...', cnt)
        time.sleep(10)

doTest1 = False
if doTest1:
    # here one thread for the scenario to generate a five-door event
    t_door = Thread(target=do_door, args=(q, scen))
    t_door.setDaemon(True)
    t_door.start()
    # here one thread for the scenario to generate a five-door event
    t_mind = Thread(target=do_mind, args=(q, mind))
    t_mind.setDaemon(True)
    t_mind.start()
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

    t_door.join()
    t_mind.join()
    print('\nAll done...')
else:
    # here each sense has its own queue
    dummy.eye.pause()
    dummy.ear.pause()
    dummy.nose.pause()
    dummy.tongue.pause()
    dummy.body.pause()
    print('test being with thread')
    cnt = 0
    startThread = True
    if startThread:
        dummy.run(startThread)
    else:   # sequential run, easy to debug
        for j in (1,20):
            scen.post(dummy.tqueue)
            dummy.run(startThread)

    # while True:
    #     cnt += 1
    #     time.sleep(10)
    #     if cnt>10:
    #         break

    print('done!')