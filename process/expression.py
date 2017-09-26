# Being's expression:
#     An act, verbal, or body, or mind
#     plus a sequence of citta (with cetasikas), and produced matter
#

import datetime as dt

class Expression(object):
    def __init__(self, being, startDT, endDT, locname, objname, scenname):
        self.being = being   # a name or tag
        # self.duration = duration  # two strings for start and end datetime
        self.start_dt = startDT  # to simplify datetime handling for now
        self.end_dt = endDT
        self.locname = locname   # a name or tag
        self.objname = objname   # a name
        self.scenname = scenname   # by name
        self.score = 0  # numerical scale 0 to 10
        self.obj = None
        self.scen = None
        self.tag = startDT + '!' + endDT + '!'+ locname + '!' + objname  + '!' + scenname   # Expression tag

    def recall(self):
        # here all relevant objects are recalled or loaded
        self.obj = self.being.loadObj(self.objname)
        self.scen = self.being.loadObj(self.scenname)

    def remember(self):
        # save all relevant objects and put in a link-tag
        self.being.memorize(self.tag, self)
        # do we have a generic mechanism to save an object?