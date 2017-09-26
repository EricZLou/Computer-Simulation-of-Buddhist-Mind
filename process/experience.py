# Being's experience:
#     time durations, location, object, scenario,
#     plus a sequence of citta (with cetasikas), and ethics score
#     Or a sequence of verbal, body, and mind expressions

import datetime as dt

class Experience(object):
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
        self.tag = startDT + '!' + endDT + '!'+ locname + '!' + objname  + '!' + scenname   # experience tag

    def recall(self):
        # here all relevant objects are recalled or loaded
        self.obj = self.being.loadObj(self.objname)
        self.scen = self.being.loadObj(self.scenname)

    def remember(self):
        # save all relevant objects and put in a link-tag
        self.being.memorize(self.tag, self)
        # do we have a generic mechanism to save an object?