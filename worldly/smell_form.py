# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj


class SmellForm(RupaObj):
    def __init__(self,  intensity, smell):
        RupaObj.__init__(self, datetime.datetime.now())
        self.intensity = intensity
        self.smell = smell
        super().addFeature('intensity', intensity)
        super().addFeature('smell', smell)