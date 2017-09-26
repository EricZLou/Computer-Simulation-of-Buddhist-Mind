# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


from enum import Enum
import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class TasteType(Enum):
    sweet = 1
    sour = 2
    salty = 3
    pungent = 4
    bitter = 5
    astringent = 6


class TasteForm(RupaObj):
    sense_type = SenseType.tongue

    def __init__(self, taste, richness, tclock):
        super().__init__(tclock)
        self.taste = taste  # Enum
        self.richness = richness
        super().addFeature('taste', taste)
        super().addFeature('richness', richness)
        self.basetype = DoorType.tongue

    def makejson(self):
        jdic = super().makejson()
        return {'class':'TasteForm', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.taste == self.taste:
            measure += 10
        measure += min(10,self.richness/obj0.richness+obj0.richness/self.richness-1)
        return measure/2.0  #scale to max of 10