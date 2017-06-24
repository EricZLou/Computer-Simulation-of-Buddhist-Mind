# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj


class TouchForm(RupaObj):
    def __init__(self, temp, texture):
        RupaObj.__init__(self, datetime.datetime.now())
        self.temp = temp
        self.texture = texture
        super().addFeature('temp', temp)
        super().addFeature('texture', texture)