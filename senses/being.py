# Being placeholder: sense organs, obj/features repositories, TQueue
# memory and TQueue could be separated into brain object

import json
from process.memory import *
from process.queue import *
from process.basics import *
from process.bavanga import Bavanga
from process.door_process import FiveDoorProcess
from process.mind_process import MindProcess

class Being(object):
    def __init__(self, eye, ear, nose, tongue, body, citta0, brain=None):
        self.eye = eye
        self.ear = ear
        self.nose = nose
        self.tongue = tongue
        self.body = body
        self.bavanga = Bavanga(citta0)
        self.brain = brain
        self.feature_mem = FeatureMemory(self)
        self.obj_mem = ObjectMemory(self)
        self.tqueue = TQueue()

        # obselete
        self.obj_dic = {}  # short term memory is a loaded object dic
        # long term meomory is stored as features and composition of features
        #  each feature is in fact a separate obj, not necessarily simple
        # such a composition is based on labels so the complete object takes time
        # to load, naturally a memory recall process
        self.features_dic = {}  # dic of key-dic pair

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

    def addFeature(self, name, fdic):
        # name of the feature, fdic: dic of key-value
        # for a composite, the value should be set to 'obj'
        self.features_dic[name]=fdic

    def addObj(self, label, obj):
        # label consists of name and instance id, e.g., 'tree_109'
        self.obj_dic[label]=obj

    def getObj(self, label):
        return self.obj_dic[label]

    def getFeature(self, key):
        return self.features_dic[key]

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
            return proc.run()
        else:
            proc = FiveDoorProcess(self, e.basetype, e.obj, e.env, ticks_passed)
            return proc.run()

    # def loadObj(self, features):
    #     # load an obj given a list of features (keys)
    #     for f in features:
    #         dic = self.features_dic[f] #the value is a dic
    #         for key, value in dic:
    #             if value == 'obj':
    #                 # f is an obj/composite namerecursive
    #                 features1 = self.features_dic[key]
    #                 self.loadObj(features1)
    #             else:
    #                 print('don not know what to do yet')
    #                 # how do we store it?
    #                 # need to think of a data structure