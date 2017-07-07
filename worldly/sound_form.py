# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class SoundForm(RupaObj):
    sense_type = SenseType.ear

    def __init__(self, loudness, pitch, frequency):
        RupaObj.__init__(self)
        self.loudness = loudness
        self.frequency = frequency
        self.pitch = pitch
        super().addFeature('loudness', loudness)
        super().addFeature('frequency', frequency)
        super().addFeature('pitch', pitch)
        self.basetype = DoorType.ear

    def makejson(self):
        jdic = super().makejson()
        return {'class':'SoundForm', 'data':jdic}

