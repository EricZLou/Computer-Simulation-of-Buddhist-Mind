# Being placeholder: sense organs and obj/features repositories


class Being(object):
    def __init__(self, eye, ear, nose, tongue, body, bavanga, brain=None):
        self.eye = eye
        self.ear = ear
        self.nose = nose
        self.tongue = tongue
        self.body = body
        self.bavanga = bavanga
        self.brain = brain
        self.obj_dic = {}  # short term memory is a loaded object dic
        # long term meomory is stored as features and composition of features
        #  each feature is in fact a separate obj, not necessarily simple
        # such a composition is based on labels so the complete object takes time
        # to load, naturally a memory recall process
        self.features_dic = {}  # dic of key-dic pair

    def addFeature(self, name, fdic):
        # name of the feature, fdic: dic of key-value
        # for a composite, the value should be set to 'obj'
        self.features_dic[name]=fdic

    def addObj(self, name, obj):
        self.obj_dic[name]=obj

    def getObj(self, key):
        return self.obj_dic[key]

    def getFeature(self, key):
        return self.features_dic[key]

    def loadObj(self, features):
        # load an obj given a list of features (keys)
        for f in features:
            dic = self.features_dic[f] #the value is a dic
            for key, value in dic:
                if value == 'obj':
                    # f is an obj/composite namerecursive
                    features1 = self.features_dic[key]
                    self.loadObj(features1)
                else:
                    # how do we store it?
                    # need to think of a data structure