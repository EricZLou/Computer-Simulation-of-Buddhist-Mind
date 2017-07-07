# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class TasteForm(RupaObj):
    sense_type = SenseType.tongue

    def __init__(self, taste, temprature, richness):
        RupaObj.__init__(self)
        self.temprature = temprature
        self.taste = taste
        self.richness = richness
        super().addFeature('temprature', temprature)
        super().addFeature('taste', taste)
        super().addFeature('richness', richness)
        self.basetype = DoorType.tongue

    def makejson(self):
        jdic = super().makejson()
        return {'class':'TasteForm', 'data':jdic}

