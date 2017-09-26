# test worldly objects in a scenario

from worldly.scenario import Scenario
from worldly.visible_form import VisibleForm, VisibleColor, VisibleShape
from worldly.sound_form import SoundForm, SoundType
from worldly.touch_form import TouchForm, TouchType
from worldly.smell_form import SmellForm, SmellType
from worldly.taste_form import TasteForm, TasteType
from worldly.env import Env

# this has only visible forms
def get_scen():
    # create objects appearing in a scenario
    tree = VisibleForm(VisibleShape.round, VisibleColor.blue, 10)
    gun = VisibleForm(VisibleShape.long, VisibleColor.yellow, 10)
    car = VisibleForm(VisibleShape.long, VisibleColor.red, 8)
    person = VisibleForm(VisibleShape.short, VisibleColor.white, 8)
    dog = VisibleForm(VisibleShape.uneven, VisibleColor.darkness, 2)

    # create an env
    env = Env(10, 10, 10, 10)
    # create a scenario and print it out
    scen = Scenario(env, 'House')
    scen.addObj(tree)
    scen.addObj(gun)
    scen.addObj(car)
    scen.addObj(person)
    scen.addObj(dog)
    return scen

# this scenario has 5 doors
def get_scen5():
    # create objects appearing in a scenario
    tree = VisibleForm(VisibleShape.round, VisibleColor.blue, 10)
    person = VisibleForm(VisibleShape.short, VisibleColor.white, 8)
    dog = VisibleForm(VisibleShape.uneven, VisibleColor.darkness, 2)

    gunshot = SoundForm(SoundType.NonconsciousNotbeingDisagreeable, 10, 'pitch_high','freq_high')
    bug = TouchForm(TouchType.lightness, 4, 'buggy')
    smoke = SmellForm(SmellType.bad, 4)
    food = TasteForm(TasteType.pungent, 6)

    # create an env
    env = Env(10, 10, 10, 10)
    # create a scenario and print it out
    scen = Scenario(env, 'House')
    scen.addObj(tree)
    scen.addObj(gunshot)
    scen.addObj(bug)
    scen.addObj(smoke)
    scen.addObj(food)
    scen.addObj(person)
    scen.addObj(dog)
    return scen

myscen = get_scen()
myscen.print()
