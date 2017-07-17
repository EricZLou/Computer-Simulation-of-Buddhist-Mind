# Features memory, implemented as a set of names, i.e., labels
# Object memory: a dictionary of keys (object name) and JSON string

#import json
#import utils.jsonencoder as jshelper
from worldly.factory import makeObjectFromDict

class FeatureMemory(object):
    def __init__(self, being):
        self.being = being
        self.features = set()

    def addFeature(self, name):
        self.features.add(name)

    def hasFeature(self, name):
        return self.features.issubset(name)


class ObjectMemory(object):
    match_floor = 0.9
    match_perfect = 1.0
    # Object repo is a dict of name-serialized_obj_string (JSON)
    def __init__(self, being):
        self.being = being
        self.objects = {}   # start with empty dict

    def addObject(self, name, featdct):
        self.objects[name]= featdct

    def minmatch(self, features):
        # given a list of features, go thr the obj repo to find a min match
        for key in self.objects: #key is label,i.e., name plus iid
            value1 = self.objects[key]
            # obj = json.loads(value1, object_hook=jshelper.makeobj) #
            obj = makeObjectFromDict(value1['class'],value1['data']) #
            score1 = obj.matchFeature(features)
            if score1 > ObjectMemory.match_floor:
                return obj
        return None

    def bestmatch(self, features):
        # given a list of features, go thr the obj repo to find a best match
        score0 = 0.0
        obj0 = None
        for key in self.objects: #key is label,i.e., name plus iid
            value1 = self.objects[key]
            # obj = json.loads(value1, object_hook=jshelper.makeobj) #
            obj = makeObjectFromDict(value1['class'],value1['data']) #
            score1 = obj.matchFeature(features)
            if score1 > score0:
                obj0 = obj
                score0 = score1
        return [score0, obj0]

    def exactmatch(self, features):
        # given a list of features, go thr the obj repo to find a best match
        score0, obj0 = self.bestmatch(features)
        if score0 >= ObjectMemory.match_perfect:
            return obj0
        return None # throw
