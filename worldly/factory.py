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
        shape=cdict['shape']
        color=cdict['color']
        size=cdict['size']
        return VisibleForm(shape, color, size)
    elif cname == 'SoundForm':
        soundtype=cdict['soundtype']
        loudness=cdict['loudness']
        pitch=cdict['pitch']
        frequency=cdict['frequency']
        return SoundForm(soundtype, loudness, pitch, frequency)
    elif cname == 'SmellForm':
        smell = cdict['smell']
        intensity = cdict['intensity']
        return SmellForm(smell, intensity)
    elif cname == 'TasteForm':
        taste=cdict['taste']
        richness=cdict['richness']
        return TasteForm(taste, richness)
    elif cname == 'TouchForm':
        touchtype=cdict['touchtype']
        pressure=cdict['pressure']
        texture=cdict['texture']
        return TouchForm(touchtype, pressure, texture)
    else:
        return None