#
# Purpose: Factory class creates an obj given a class name and dict.
#

from worldly.visible_form import VisibleForm
from worldly.sound_form import SoundForm
from worldly.taste_form import TasteForm
from worldly.smell_form import SmellForm
from worldly.touch_form import TouchForm

def makeObjectFromDict(cname, cdict0):
    cdict = cdict0['FEAT']
    if cname == 'VisibleForm':
        size=cdict['size']
        shape=cdict['shape']
        color=cdict['color']
        return VisibleForm(size, shape, color)
    elif cname == 'SoundForm':
        loudness=cdict['loudness']
        pitch=cdict['pitch']
        frequency=cdict['frequency']
        return SoundForm(loudness, pitch, frequency)
    elif cname == 'SmellForm':
        intensity = cdict['intensity']
        smell = cdict['smell']
        return SmellForm(intensity, smell)
    elif cname == 'TasteForm':
        taste=cdict['taste']
        temprature=cdict['temprature']
        richness=cdict['richness']
        return TasteForm(taste, temprature, richness)
    elif cname == 'TouchForm':
        pressure=cdict['pressure']
        texture=cdict['texture']
        return TouchForm(pressure, texture)
    else:
        return None