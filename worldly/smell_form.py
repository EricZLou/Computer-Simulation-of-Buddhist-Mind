# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj
from process.basics import *


class SmellForm(RupaObj):
    sense_type = SenseType.nose

    def __init__(self,  intensity, smell):
        super().__init__()
        self.intensity = intensity
        self.smell = smell
        super().addFeature('intensity', intensity)
        super().addFeature('smell', smell)
        self.basetype = DoorType.nose

    def makejson(self):
        jdic = super().makejson()
        return {'class':'SmellForm', 'data':jdic}

