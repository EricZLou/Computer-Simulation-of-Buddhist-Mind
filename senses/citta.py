# citta base:
#     a citta has a callback function that does the work when citta arises

from process.basics import *
from senses.cetasika import CetasikaType as CE


class Citta(object):

    def __init__(self, obj=None, base=None):
        # list of cetasikas by enums. init with universals. other to add
        self.cetasikas = [CE.Contact, CE.Feeling, CE.Perception, CE.Volition, CE.One_pointedness,
                          CE.Life_faculty, CE.Attention]
        self.obj = obj   # sense obj or mind obj, not visible form etc.
        self.base = base  # base obj, not basetype!
        self.being = None
        self.wsness = Wholesomeness.variable  # enum
        self.callback_func = None
        self.debug = True

    # callback function takes an obj and returns what?
    def setcallback(self, func):
        self.callback_func = func

    def arise(self):
        if self.callback_func is not None:
            return self.callback_func(self.obj)
        return None

    def decay(self):
        if self.obj is not None:
            self.obj.tick()

    # callback function takes an obj and returns what?
    def setBeing(self, being):
        self.being = being

    # arise then decay
    def go(self):
        temp = self.arise()
        self.decay()
        return temp

    def addCetasika(self, cenum):
        self.cetasikas.append(cenum)