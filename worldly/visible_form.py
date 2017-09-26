# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects

from enum import IntEnum
from worldly.rupa_object import RupaObj
from process.basics import *
import utils.jsonencoder as jut


# from Abhidharmavatara
class VisibleColor(IntEnum):
    blue = 1
    yellow = 2
    red = 3
    white = 4
    cloud = 5
    smoke = 6
    dust = 7
    mist = 8
    shadow = 9
    sunlight = 10
    luminosity = 11
    darkness = 12

class VisibleShape(IntEnum):
    long = 1
    short = 2
    square = 3
    round = 4
    high = 5
    low = 6
    even = 7  # regular shape
    uneven = 8


class VisibleForm(RupaObj):
    sense_type = SenseType.eye

    def __init__(self,  shape, color, size, tclock, distance=0):
        super().__init__(tclock)
        self.shape = shape  # VisibleShape
        self.color = color   # VisibleColor
        self.size = size
        self.distance = distance
        super().addFeature('shape', shape)
        super().addFeature('color', color)
        super().addFeature('size', size)
        super().addFeature('distance', distance)
        self.basetype = DoorType.eye

    def makejson(self):
        jdic = super().makejson()
        return {'class':'VisibleForm', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.color == self.color:
            measure += 10
        if not self.shape == obj0.shape:
            measure += 10
        # could incorporate size change as well.
        measure += min(10, self.size/obj0.size+obj0.size/self.size-1)
        return measure/3.0  #scale to max of 10