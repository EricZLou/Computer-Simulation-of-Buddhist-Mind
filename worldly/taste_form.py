# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from rupa_object import RupaObj
from process.basics import *


class TasteForm(RupaObj):
    sense_type = SenseType.tongue

    def __init__(self, temp, taste, texture):
        RupaObj.__init__(self, datetime.datetime.now())
        self.temp = temp
        self.taste = taste
        self.texture = texture
        super().addFeature('temp', temp)
        super().addFeature('taste', taste)
        super().addFeature('texture', texture)