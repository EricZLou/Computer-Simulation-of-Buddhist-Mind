# mind, container for mind door events
#       each being has one mind
#       this takes care of spontaneous mind events.
#       Mind events are also generated during Javana process

import time
import numpy.random as Ran
from senses.events import *
from senses.sense_object import *
from senses.ticked_object import TickedObj


class MindObject(TickedObj):
    def __init__(self, idx):
        super().__init__(time.time())
        self.idx = idx

    # return num of seconds lapsed since object created
    def timelapsed(self, time1=0):
        if time1 > 0:
            return time1 - self.startdt
        else:
            return time.time() - self.startdt

    # return num of seconds lapsed since object created
    def ticklapsed(self, time1=0):
        tm = self.timelapsed(time1)
        ticks = int(tm/g_tick_time) % g_tick_units
        return ticks


class Mind(object):
    def __init__(self, being):
        self.being = being
        # need a definition of mind obj!

    def run(self, time1):
        # generate random events and post to queue. This is not a loop.
        #nobj = len(self.objs)
        #iobj = Ran.randint(0, nobj)
        #obj = self.objs[iobj]
        iobj = Ran.randint(0, 1000)
        # treating object itself as an event
        # compute ticks passed
        obj = MindObject(iobj)
        ticks = obj.ticklapsed(time1)
        evt = MindEvent(obj, time1, ticks)
        return evt

    def post(self, q):
        # this posts sense events from this scenario to central queue q
        time1 = time.time()
        evt = self.run(time1)
        q.post(evt)
