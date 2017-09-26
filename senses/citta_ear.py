# citta eye
from enum import Enum
from process.basics import *
from senses.citta_sense import CittaSense
from senses.sense_object import *


# features directly known to eye consciousness
class CittaEarTraits(Enum):
    soundtype = 0
    loudness = 1
    frequency = 2
    pitch = 3

# eye consciousness
class CittaEar(CittaSense):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, air):
        super().__init__(base, vobj)
        self.sobj = SenseObjEar(base, vobj, air, vobj.tickclock)

    def getsoundtype(self):
        return self.sobj.obj.soundtype

    def getloudness(self):
        return self.sobj.obj.loudness

    def getfrequency(self):
        return self.sobj.obj.frequency

    def getpitch(self):
        return self.sobj.obj.pitch

    def getTrait(self, trait):
        if trait in CittaEarTraits.__members__:
            return self.sobj.obj.features[trait]
        else:
            print('Bad trait')