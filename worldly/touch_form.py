# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from enum import Enum
from worldly.rupa_object import RupaObj
from process.basics import *


class TouchType(Enum):
    smoothness = 1
    coarseness = 2
    heaviness = 3
    lightness = 4
    coldness = 5
    hunger = 6
    thirst = 7

class TouchForm(RupaObj):
    sense_type = SenseType.body

    def __init__(self, touchtype, pressure, texture, tclock):
        super().__init__(tclock)
        self.touchtype = touchtype
        self.pressure = pressure
        self.texture = texture
        super().addFeature('touchtype', touchtype)
        super().addFeature('pressure', pressure)
        super().addFeature('texture', texture)
        self.basetype = DoorType.body

    def makejson(self):
        jdic = super().makejson()
        return {'class':'TouchForm', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.touchtype == self.touchtype:
            measure += 10
        measure += min(10,self.pressure/obj0.pressure+obj0.pressure/self.pressure-1)
        return measure/2.0  #scale to max of 10