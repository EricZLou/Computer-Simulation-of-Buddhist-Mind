# Being placeholder:
#   Sense organs, obj/features repositories, TQueue
#   memory and TQueue could be separated into brain object
#   central queue and sense queue: sense queue event repost to central only when pulled


import json
import time
from threading import Thread
from process.memory import *
from process.queue import *
from process.basics import *
from process.bavanga import Bavanga
from process.door_process import FiveDoorProcess
from process.mind_process import MindProcess
from process.mind import Mind
import process.globalvar as gvar
from worldly.visible_form import VisibleForm, VisibleColor, VisibleShape
from worldly.sound_form import SoundForm, SoundType
from worldly.touch_form import TouchForm, TouchType
from worldly.smell_form import SmellForm, SmellType
from worldly.taste_form import TasteForm, TasteType

class Being(object):
    def __init__(self, eye, ear, nose, tongue, body, tclock, interval=gvar.g_thread_interval):
        self.eye = eye  #SenseEye object
        self.ear = ear   #SenseEar object etc.
        self.nose = nose
        self.tongue = tongue
        self.body = body
        self.interval = interval
        self.pausing = False  # could toggle on/off on the sense
        self.dead = False
        self.bavanga = Bavanga(None)
        self.tclock = tclock
        self.feature_mem = FeatureMemory(self)
        self.obj_mem = ObjectMemory(self)
        self.tqueue = TQueue()  #central queue
        self.mind = Mind(self)  # mind object
        self.scenario = None
        self.iniObjects()  #initial objects for each sense
        # threadrun = Thread(target=self.run, args=())
        # threadrun.daemon = True          # Daemonize thread
        self.realtime = False   # false to run ticked mode to allow manipulation
        # threadrun.start()                # Start the execution
        if self.realtime:
            self.threadpost = Thread(target=self.post, args=())
            self.threadpost.daemon = True          # Daemonize thread
        else:
            self.threadpost = None
        #threadpost.join()
        self.javana_citta = None
        self.javana_callback = None
        self.regis_citta = None
        self.regis_callback = None

    def base(self, basetype):
        if basetype == SenseType.eye:
            return self.eye
        elif basetype == SenseType.ear:
            return self.ear
        elif basetype == SenseType.nose:
            return self.nose
        elif basetype == SenseType.tongue:
            return self.tongue
        elif basetype == SenseType.body:
            return self.body
        else:
            return self.bavanga  # as the mind base

    def setjavana(self, jav, cfunc):
        self.javana_citta = jav
        self.javana_callback = cfunc

    def setregistration(self, regiscitta, cfunc):
        self.regis_citta = regiscitta
        self.regis_callback = cfunc

    def memorize(self, obj):
        # do two things: 1) if new feature, add it to featurememory, 2) add to object memory
        jmsg = obj.makejson()
        self.feature_mem.addFeature(obj.name) # feature doesn't have iid
        self.obj_mem.addObject(obj.label(), jmsg)
        # might need to recursively add keys and objects

    def recall(self, features, bestmatch=True):
        if bestmatch:
            rslt = self.obj_mem.bestmatch(features)
            return rslt[1] # [0] has the score
        else:
            return self.obj_mem.minmatch(features)

    def process(self, e, ticks_passed):
        # runs bavanga or any other processes on event e
        if e.basetype == DoorType.mind:
            proc = MindProcess(self, e.obj, ticks_passed)  # here e is the senseobj
        else:
            # print(e.basetype)
            proc = FiveDoorProcess(self, e.basetype, e.obj, e.env, ticks_passed)
        proc.being = self
        if self.javana_citta is not None:
            proc.javana_citta = self.javana_citta
            proc.javana_citta.callback_func = self.javana_callback
        if self.regis_citta is not None:
            proc.regis_citta = self.regis_citta
            proc.regis_citta.callback_func = self.regis_callback
        return proc.run()

    def pause(self, pausing=True):
        self.pausing = pausing

    def die(self):
        self.dead = True

    def run(self, startQueue=True):
        if startQueue:
            self.threadpost.start()                # Start the execution
            while not self.dead:
                if not self.tqueue.isempty():
                    e = self.tqueue.get()
                    ticks = e.obj.ticklapsed()
                    self.process(e, ticks)
                if self.realtime:
                    time.sleep(self.interval)
            print('Person dead...')
        else:
            if not self.dead and not self.tqueue.isempty():
                e = self.tqueue.get()
                ticks = e.obj.ticklapsed()
                self.process(e, ticks)
                if self.realtime:
                    time.sleep(self.interval)

    def post(self):
        while not self.dead:
            if not self.pausing:
                if not self.scenario is None:
                    self.scenario.post_door(self)
                if self.realtime:
                    time.sleep(self.interval)
                self.mind.post(self.tqueue)
            else:
                print('Person in coma...')
                if self.realtime:
                    time.sleep(self.interval*5)  # sleep longer

        print('Person dead...')

    #if there is a pull, post to central queue
    def dopull(self, sensebase, evt):
        obj1 = evt.obj
        haspull = sensebase.impinge(obj1)
        if haspull:
            print('central queue pulled in scenario.')
            self.tqueue.post(evt)
        else:
            print('no pull observed.')

    def bindScenario(self, scen):
        self.scenario = scen
        if self.eye is not None:
            self.eye.bindScenario(scen)
        if self.ear is not None:
            self.ear.bindScenario(scen)
        if self.nose is not None:
            self.nose.bindScenario(scen)
        if self.tongue is not None:
            self.tongue.bindScenario(scen)
        if self.body is not None:
            self.body.bindScenario(scen)

    # post_door gets called from scenario.post_door
    # given an event, route to the sense and handle pull as is
    # to use this function, sense (eye etc)'s thread should be disabled
    def post_door(self, evt):
        btype = evt.basetype
        if (btype == DoorType.eye) and (self.eye is not None):
            print('visible form posted to eye ...')
            self.dopull(self.eye, evt)
            self.eye.post(evt)  #post and update obj
        elif (btype == DoorType.ear) and (self.ear is not None):
            print('sound form posted to ear ...')
            self.dopull(self.ear, evt)
            self.ear.post(evt)
        elif (btype == DoorType.nose) and (self.nose is not None):
            print('smell form posted to nose ...')
            self.dopull(self.nose, evt)
            self.nose.post(evt)
        elif (btype == DoorType.tongue) and (self.tongue is not None):
            print('taste form posted to tongue ...')
            self.dopull(self.tongue, evt)
            self.tongue.post(evt)
        elif (btype == DoorType.body) and (self.body is not None):
            print('touch posted to body ...')
            self.dopull(self.body, evt)
            self.body.post(evt)  #post and update obj
        else:  #mind door
            print('obj posted to mind ...')
            self.tqueue.post(evt)

    def iniObjects(self):
        if self.eye is not None:
            self.eye.obj_bound = VisibleForm(VisibleShape.even,VisibleColor.sunlight,0.1, self.tclock)
        if self.ear is not None:
            self.ear.obj_bound = SoundForm(SoundType.ConsciousBeingAgreeable,0.1,'low',10, self.tclock)
        if self.nose is not None:
            self.nose.obj_bound = SmellForm(SmellType.neutral,0.1, self.tclock)
        if self.tongue is not None:
            self.tongue.obj_bound = TasteForm(TasteType.salty,0.1, self.tclock)
        if self.body is not None:
            self.body.obj_bound = TouchForm(TouchType.coldness, 0.1,'none', self.tclock)
