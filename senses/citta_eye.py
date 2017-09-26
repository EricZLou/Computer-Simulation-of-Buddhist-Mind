# citta eye
from enum import Enum
from process.basics import *
from senses.citta_sense import CittaSense
from senses.sense_object import *


# features directly known to eye consciousness
class CittaEyeTraits(Enum):
    color = 0
    shape = 1
    size = 2   # or dimension
    distance = 3


# eye consciousness
class CittaEye(CittaSense):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, light):
        super().__init__(base, vobj)
        self.sobj = SenseObjEye(base, vobj, light, vobj.tickclock)

    def getColor(self):
        return self.sobj.obj.color

    def getSize(self):
        return self.sobj.obj.size

    def getShape(self):
        return self.sobj.obj.shape

    def getDistance(self):
        return self.sobj.obj.distance

    def getTrait(self, trait):
        if trait in CittaEyeTraits.__members__:
            return self.sobj.obj.features[trait]
        else:
            print('Bad trait')