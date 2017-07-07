# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sensory organ's image of these rupa objects

import json
import time
from process.basics import *
from utils.dicthelper import *
from process.globalvar import *

class RupaObj(object):
    instance_id = 0
    def __init__(self):
        # dt is sampling datetime
        self.startdt = time.time() # epoch time (in sec) when obj is created
        self.name = 'null'  #obj identified by a name or concept
        self.features_dc = {} # dictionary of things
        self.desirable = ObjectDesirable.desirable # this causes equinimity/neutral
        RupaObj.instance_id += 1
        self.instance_id = RupaObj.instance_id
        self.basetype = DoorType.mind

    def addFeature(self, key, value):
        self.features_dc[key]=value

    def features(self):
        #features defining the obj
        return self.features_dc

    def label(self):
        return self.name + '_' + str(self.instance_id)

    def match(self, obj):
        # same instance_id-->same as self; same name-->match; no name-->compare features
        if obj.instance_id == self.instance_id:
            return True
        elif (obj.name == self.name) & self.name != 'null':
            return True
        else:
            return False

    def matchFeature(self, features):
        return matchFeature(self.features_dc, features)

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

    # def serialize(self):
    #     jmsg = json.dumps(self)
    #     return jmsg
    #
    def makejson(self):
        jdic = {'name': self.name, 'iid':self.instance_id, 'desirable':self.desirable.value, 'FEAT':self.features_dc}
        return jdic # or dict('RupaObj':jdic) or jdic to skip base class name!

    def print(self):
        print(self.name)
        print(self.desirable)
        for kv in self.features_dc.items():
            print(kv[0]+ ":", kv[1])