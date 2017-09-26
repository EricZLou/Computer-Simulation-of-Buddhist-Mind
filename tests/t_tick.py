# tick on the twig
import time
import numpy.random as Ran
from threading import Thread
import sys
from process.queue import TQueue
from process.mind import Mind
from worldly.visible_form import VisibleForm, VisibleColor, VisibleShape
from worldly.touch_form import TouchForm, TouchType
from worldly.smell_form import SmellForm, SmellType, SmellOdor
from worldly.taste_form import TasteForm, TasteType
from worldly.env import Env
from worldly.scenario import Scenario
from senses.tick import BeingTick
from senses.sense_base import *
from senses.citta_javana import JavanaCitta
from senses.citta_invg import RegistrationCitta
from senses.ticked_object import TickClock


tickclock = TickClock()  # a global tick clock
# create a tick
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
ta = BeingTick(nose, tongue, body, tickclock)


def forrest(tclock):
    # a tree, many animals passing by in a forrest setting
    # here, create one animal but allows its smell to randomly change
    tree = VisibleForm(VisibleShape.round, VisibleColor.blue, 10, tclock)
    bug = TouchForm(TouchType.lightness, 4, 'buggy', tclock)
    person = SmellForm(SmellType.good, 8, tclock)
    dog = SmellForm(SmellType.bad, 8, tclock)
    poo = SmellForm(SmellType.bad, 9, tclock)
    food = SmellForm(SmellType.good, 6, tclock)

    # create an env
    env = Env(10, 10, 10, 10)
    # create a scenario and print it out
    scen = Scenario(tclock, env, 'Forrest')
#    scen.addObj(tree)
    scen.addObj(bug)
#    scen.addObj(person)
#    scen.addObj(dog)
#    scen.addObj(poo)
#    scen.addObj(food)
    return scen


scen = forrest(tickclock)
scen.realtime = False
ta.bindScenario(scen)
q = TQueue()  # central queue
jav = JavanaCitta(SenseType.nose, ta.tqueue)  # bind to ta's tqueue
ta.setjavana(jav, ta.onJavana)
regiscitta = RegistrationCitta()  # bind to ta's tqueue
regiscitta.setBeing(ta)
ta.setregistration(regiscitta, ta.onRegistration)

# control the scen with animal entries
max_interval = 100 # ticks
animal = SmellOdor(SmellType.good, 10, 'other', tickclock)

startThread = False
if startThread:
    ta.run(startThread)
else:  # sequential run, easy to debug
    #while True:
    ta.realtime = False
    odor_list = list(BeingTick.body_odor.keys())
    for j in range(1000):
        t_interval = Ran.randint(0, max_interval)
    #    time.sleep(t_interval*g_tick_time)
        i_odor = Ran.randint(0, BeingTick.nb_odor)
        odorstr = odor_list[i_odor]
        #favor = BeingTick.body_odor.values()[i_odor]
        # make intensity random as well
        odor_intensity = Ran.randint(1, 10)
        animal.set_intensity(odor_intensity)
        animal.set_odor(odorstr)
        # animal.odor = odorstr  # bad, dic not updated
        # note favor or not is treated as a javana experience
        # now let the animal enter the forrest
        scen.addObj(animal)
        # need to post events out of the run thread for testing purposes
        evt = scen.post(ta.tqueue)
        # how long the animal stays before it leaves
        animal_stay = Ran.randint(1, 10)  # stay in ticks
        #ta.run(startThread)
        # try javana processing
        #jav.arise()
        ta.run(False)
        tickclock.sleep(5)  # number of ticks to sleep on
    #    time.sleep(animal_stay*g_tick_time)
        scen.removeObj(animal)   # animal leaves

# define a forest where animals roam randomly
def forest2():
    print('nothing')