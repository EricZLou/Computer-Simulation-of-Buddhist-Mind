# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class TouchForm(RupaObj):
    sense_type = SenseType.body

    def __init__(self, pressure, texture):
        RupaObj.__init__(self)
        self.pressure = pressure
        self.texture = texture
        super().addFeature('pressure', pressure)
        super().addFeature('texture', texture)
        self.basetype = DoorType.body

    def makejson(self):
        jdic = super().makejson()
        return {'class':'TouchForm', 'data':jdic}
