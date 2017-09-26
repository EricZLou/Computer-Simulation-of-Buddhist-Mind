# citta eye
from enum import Enum
from process.basics import *
from senses.citta_sense import CittaSense
from senses.sense_object import *


# features directly known to eye consciousness
class CittaTongueTraits(Enum):
    taste = 0
    richness = 1


# eye consciousness
class CittaTongue(CittaSense):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, water):
        super().__init__(base, vobj)
        self.sobj = SenseObjTongue(base, vobj, water, vobj.tickclock)

    def arise(self):
        # evaluate strength
        self.sobj.computeObjGreatness()
        return

    def gettaste(self):
        return self.sobj.obj.taste

    def getrichness(self):
        return self.sobj.obj.richness

    def getTrait(self, trait):
        if trait in CittaTongueTraits.__members__:
            return self.sobj.obj.features[trait]
        else:
            print('Bad trait')