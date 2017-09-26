#
# Purpose: Scenario class creates a scenario where senses come into play
#
import time
import numpy.random as Ran
from senses.events import SenseEvent
from senses.ticked_object import TickedObj


class Scenario(TickedObj):
    # need to maintain a clock
    def __init__(self, tclock, env=None, theme='none'):
        super().__init__(tclock, 1E10)  # 1E10 longest time
        self.theme = theme
        self.env = env
        self.objs = []  # obj list

    def addObj(self, obj):
        # obj.bindScenario(self)
        self.objs.append(obj)

    def removeObj(self, obj):
        # obj.bindScenario(self)
        self.objs.remove(obj)

    def run(self):
        # generate random events and post to queue. This is not a loop.
        nobj = len(self.objs)
        if nobj < 2:
            iobj = 0
        else:
            iobj = Ran.randint(0, nobj)
        obj = self.objs[iobj]
        # treating object itself as an event
        # compute ticks passed
        ticks = obj.ticklapsed()
        time1 = self.tickclock.current()
        evt = SenseEvent(obj.basetype, obj, self.env, time1, ticks)
        return evt

    def post(self, q):
        # this posts all sense events from this scenario to central queue q, not sense queue
        evt = self.run()
        q.post(evt)
        return evt

    def post_door(self, being):
        # this posts sense events from each door to being which sorts out which q
        evt = self.run()
        being.post_door(evt)
        return evt

    def print(self):
        print(self.theme)
        for obj in self.objs:
            obj.print()
