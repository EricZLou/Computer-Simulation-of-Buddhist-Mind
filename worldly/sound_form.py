# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


from enum import Enum
import datetime
from worldly.rupa_object import RupaObj
from process.basics import *

class SoundType(Enum):
    ConsciousBeingAgreeable = 1
    ConsciousBeingDisagreeable = 2
    ConsciousNotbeingAgreeable = 3
    ConsciousNotbeingDisagreeable = 4
    NonconsciousBeingAgreeable = 5
    NonconsciousBeingDisagreeable = 6
    NonconsciousNotbeingAgreeable = 7
    NonconsciousNotbeingDisagreeable = 8


class SoundForm(RupaObj):
    sense_type = SenseType.ear

    def __init__(self, soundtype, loudness, pitch, frequency, tclock):
        super().__init__(tclock)
        self.soundtype = soundtype  #Enum
        self.loudness = loudness    # on a 10 scale
        self.frequency = frequency  # digital
        self.pitch = pitch          # low, high etc.
        super().addFeature('soundtype', soundtype)
        super().addFeature('loudness', loudness)
        super().addFeature('frequency', frequency)
        super().addFeature('pitch', pitch)
        self.basetype = DoorType.ear

    def makejson(self):
        jdic = super().makejson()
        return {'class':'SoundForm', 'data':jdic}

    # override, compare with obj0 to see to evaluate impact
    def impact(self, obj0):
        measure = 0 # on a 10 scale
        if not obj0.soundtype == self.soundtype:
            measure += 10
        if not obj0.pitch == self.pitch:
            measure += 10
        measure += min(10, self.loudness/obj0.loudness+obj0.loudness/self.loudness-1)
        return measure/3.0  #scale to max of 10