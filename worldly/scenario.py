#
# Purpose: Scenario class creates a scenario where senses come into play
#
import time
import numpy.random as Ran

class SenseEvent(object):
    def __init__(self, basetype, obj, env, time1, ticks):
        self.basetype = basetype
        self.obj = obj
        self.env = env
        self.timenow = time1  # py datetime
        self.ticks_passed = ticks

class Scenario(object):
    # need to maintain a clock
    def __init__(self, env=None, theme='none'):
        self.theme = theme
        self.env = env
        self.objs = []  # obj list
        self.time0 = time.time()

    def addObj(self, obj):
        # obj.bindScenario(self)
        self.objs.append(obj)

    def run(self, time1):
        # generate random events and post to queue. This is not a loop.
        nobj = len(self.objs)
        iobj = Ran.randint(0, nobj)
        obj = self.objs[iobj]
        # treating object itself as an event
        # compute ticks passed
        ticks = obj.ticklapsed(time1)
        evt = SenseEvent(obj.basetype, obj, self.env, time1, ticks)
        return evt

    def post(self, q):
        # this posts sense events from this scenario to central queue q
        time1 = time.time()
        evt = self.run(time1)
        q.post(evt)

    def print(self):
        print(self.theme)
        for obj in self.objs:
            obj.print()
