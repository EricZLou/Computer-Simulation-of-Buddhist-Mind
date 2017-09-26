# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects

from enum import IntEnum
import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class SmellType(IntEnum):
    good = 1
    bad = 2
    neutral = 3


class SmellForm(RupaObj):
    sense_type = SenseType.nose

    def __init__(self, smell, intensity, tclock):
        super().__init__(tclock)
        self.intensity = intensity
        self.smell = smell
        super().addFeature('intensity', intensity)
        super().addFeature('smell', smell)
        self.basetype = DoorType.nose

    def makejson(self):
        jdic = super().makejson()
        return {'class':'SmellForm', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.smell == self.smell:
            measure += 10
        measure += min(10,self.intensity/obj0.intensity+obj0.intensity/self.intensity-1)
        return measure/2.0  #scale to max of 10


class SmellOdor(SmellForm):
    # body odor
    def __init__(self, smell, intensity, odor, tclock):
        super().__init__(smell, intensity, tclock)
        self.odor = odor   # body odor type, string
        super().addFeature('odor', odor)

    # need to use setters to keep dic updated
    def set_odor(self,odor):
        self.odor = odor   # body odor type, string
        super().addFeature('odor', odor)

    def set_intensity(self,intensity):
        self.intensity = intensity   # body odor type, string
        super().addFeature('intensity', intensity)

    def makejson(self):
        jdic = super().makejson()
        return {'class':'SmellOdor', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.smell == self.smell:
            measure += 10
        measure += min(10,self.intensity/obj0.intensity+obj0.intensity/self.intensity-1)
        return measure/2.0  #scale to max of 10