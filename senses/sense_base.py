# Sense base object
#   each sense maintains its own time decayed queue
#

import time
from threading import Thread
from process.queue import *
import process.globalvar as gvar
from process.basics import *


class SenseBase(object):
    runownthread = False

    def __init__(self, strength, interval=gvar.g_thread_interval):
        self.basetype = 0  #enum sensory organ as basetype
        self.interval = interval
        self.pausing = False   # could toggle on/off on the sense
        self.strength = strength  #overall strength of the sense organ
        self.tqueue = TQueue()
        self.scenario = None
        self.obj_bound = None
        #create my own thread
        if SenseBase.runownthread:
            thread = Thread(target=self.run, args=())
            thread.daemon = True          # Daemonize thread
            thread.start()                # Start the execution

    def pause(self, pausing = True):
        self.pausing = pausing

    def run(self):
        while True:
            if not self.pausing:
                if self.scenario is None:
                    print('No active scenario. sleeping...')
                    time.sleep(self.interval*5)
                else:
                    evt = self.scenario.post(self.tqueue)
                    self.obj_bound = evt.obj   #this should be bound when processing
                    time.sleep(self.interval)
            else:
                print('Sense door paused...')
                time.sleep(self.interval*10)  # sleep longer

    def bindScenario(self, scen):
        self.scenario = scen

    def post(self, evt):
        self.tqueue.post(evt)
        self.obj_bound = evt.obj  # because there is no processing so this is fine.

    # given two events on the same door, a sense organ must be able to ascertain impact
    def impinge(self, obj2):
        if self.obj_bound is not None:
            return self.obj_bound.impact(obj2) > gvar.g_impinge_score   #hard coded 8 of 10 counts as an impact
        else:
            return False


class SenseEye(SenseBase):
    # vision [left right] strength
    def __init__(self, vision):
        super().__init__(min(vision[0], vision[1]))
        self.vision = vision
        self.basetype = SenseType.eye  #enum sensory organ as base


class SenseEar(SenseBase):
    # hearing [left right] strength
    def __init__(self, hearing):
        super().__init__(min(hearing[0], hearing[1]))
        self.hearing = hearing
        self.basetype = SenseType.ear  #enum sensory organ as base


class SenseNose(SenseBase):
    # smell strength
    def __init__(self, nosesens):
        super().__init__(nosesens)
        self.nosesens = nosesens
        self.basetype = SenseType.nose  #enum sensory organ as base


class SenseTongue(SenseBase):
    # taste strength
    def __init__(self, tonguesens):
        super().__init__(tonguesens)
        self.tonguesens = tonguesens
        self.basetype = SenseType.tongue  #enum sensory organ as base


class SenseBody(SenseBase):
    # taste strength
    def __init__(self, bodysens):
        super().__init__(bodysens)
        self.bodysens = bodysens
        self.basetype = SenseType.body  #enum sensory organ as base


class SenseMind(SenseBase):
    # taste strength
    def __init__(self, mindsens):
        super().__init__(mindsens)
        self.mindsens = mindsens
        self.basetype = SenseType.mind  #enum sensory organ as base


def makeSenseBase(basetype, sens):
    if basetype == SenseType.eye:
        obj = SenseEye(sens)
    elif basetype == SenseType.ear:
        obj = SenseEar(sens)
    elif basetype == SenseType.nose:
        obj = SenseNose(sens)
    elif basetype == SenseType.tongue:
        obj = SenseTongue(sens)
    elif basetype == SenseType.body:
        obj = SenseBody(sens)
    else:
        obj = SenseMind(sens)
    return obj