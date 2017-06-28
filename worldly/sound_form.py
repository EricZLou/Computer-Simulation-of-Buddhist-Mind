# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from rupa_object import RupaObj
from process.basics import *


class SoundForm(RupaObj):
    sense_type = SenseType.ear

    def __init__(self, loudness, feeling):
        RupaObj.__init__(self, datetime.datetime.now())
        self.loudness = loudness
        self.feeling = feeling
        super().addFeature('loudness', loudness)
        super().addFeature('feeling', feeling)