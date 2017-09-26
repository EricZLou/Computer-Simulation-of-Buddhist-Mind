# citta eye
from enum import IntEnum
from process.basics import *
from senses.citta_sense import CittaSense
from senses.sense_object import *


# features directly known to eye consciousness
class CittaBodyTraits(IntEnum):
    touchtype = 0
    pressure = 1
    texture = 2


# eye consciousness
class CittaBody(CittaSense):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, earth):
        super().__init__(base, vobj)
        self.sobj = SenseObjBody(base, vobj, earth, vobj.tickclock)

    def arise(self):
        # evaluate strength
        self.sobj.computeObjGreatness()
        return

    def gettouchtype(self):
        return self.sobj.obj.touchtype

    def getpressure(self):
        return self.sobj.obj.pressure

    def gettexture(self):
        return self.sobj.obj.texture

    def getTrait(self, trait):
        if trait in CittaBodyTraits.__members__:
            return self.sobj.obj.features[trait]
        else:
            print('Bad trait')