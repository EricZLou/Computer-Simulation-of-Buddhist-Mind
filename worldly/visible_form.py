# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj


class VisibleForm(RupaObj):
    def __init__(self,  size, shape, color):
        RupaObj.__init__(self, datetime.datetime.now())
        self.size = size
        self.shape = shape
        self.color = color
        super().addFeature('size', size)
        super().addFeature('shape', shape)
        super().addFeature('color', color)