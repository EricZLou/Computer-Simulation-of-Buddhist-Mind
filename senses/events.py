#
# Purpose: Sense and mind events
#
from process.basics import *


class CognitiveEvent(object):
    def __init__(self, basetype, obj, time1, ticks):
        self.basetype = basetype
        self.obj = obj
        self.timenow = time1  # py datetime
        self.ticks_passed = ticks


class SenseEvent(CognitiveEvent):
    def __init__(self, basetype, obj, env, time1, ticks):
        super().__init__(basetype, obj, time1, ticks)
        self.env = env


class MindEvent(CognitiveEvent):
    def __init__(self, obj, time1, ticks, citta=None):
        super().__init__(DoorType.mind, obj, time1, ticks)
        self.citta = citta  # associated citta leading to this event
