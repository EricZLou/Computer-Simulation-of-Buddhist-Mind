# citta eye
from enum import Enum
from process.basics import *
from senses.citta_sense import CittaSense
from senses.sense_object import *


# features directly known to eye consciousness
class CittaNoseTraits(Enum):
    smell = 0
    intensity = 1


# eye consciousness
class CittaNose(CittaSense):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, wind):
        super().__init__(base, vobj)
        self.sobj = SenseObjNose(base, vobj, wind, vobj.tickclock)

    def arise(self):
        # evaluate strength
        self.sobj.computeObjGreatness()
        return

    def getsmell(self):
        return self.sobj.obj.smell

    def getintensity(self):
        return self.sobj.obj.intensity

    def getTrait(self, trait):
        if trait in CittaNoseTraits.__members__:
            return self.sobj.obj.features[trait]
        else:
            print('Bad trait')