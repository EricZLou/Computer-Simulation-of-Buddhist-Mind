# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from rupa_object import RupaObj
from process.basics import *


class TouchForm(RupaObj):
    sense_type = SenseType.body

    def __init__(self, temp, texture):
        RupaObj.__init__(self, datetime.datetime.now())
        self.temp = temp
        self.texture = texture
        super().addFeature('temp', temp)
        super().addFeature('texture', texture)