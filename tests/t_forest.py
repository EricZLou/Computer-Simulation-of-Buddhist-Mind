# tick on the twig
import time
import numpy as np
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
from worldly.animal import Animal
from worldly.forest import Forest

tickclock = TickClock()  # a global tick clock
np.random.seed(1000000)
# create a tick
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
ta = BeingTick(nose, tongue, body, tickclock)

# create an env
env = Env(10, 10, 10, 10)
# create a forest
fgun = Forest(tickclock, env)

num_tick = 1000 # tick population
num_life = 5  # simulate time horizon
life_nofood = 1000  # from last food to die due to hunger
time_nohunger = 500  # from last food to feel hungry
#roamrate_scale = 10000 # top scale is 10
average_arr_interval =50.0

ta.life_nofood = life_nofood  # from last food to die due to hunger
ta.time_nohunger = time_nohunger  # from last food to feel hungry
ta.time_jump = 0  # time it takes to jump off, latch on, drill blood, and get back to twig
ta.tgt_favor_food = 0 # great than this, count as a meal
# create animals
odor_list = list(BeingTick.body_odor.keys())
num_animals = len(odor_list)
average_arr_rate = 1.0/average_arr_interval/num_animals
for j in range(0, len(odor_list)):
    odor_score = BeingTick.body_odor[odor_list[j]]
    roamrate = BeingTick.body_roamrate[odor_list[j]]/5.0*average_arr_rate
    ann = Animal( odor_list[j], odor_score, roamrate)
    fgun.addAnimal(ann)

# add non-animals
# a tree, many animals passing by in a forrest setting
# here, create one animal but allows its smell to randomly change
# bloodtaste = TasteForm(TasteType.sweet, 10, tickclock)
# bugtouch = TouchForm(TouchType.lightness, 4, 'buggy', tickclock)
# grassmell = SmellForm(SmellType.neutral, 6, tickclock)
# fgun.addObj(bloodtaste)  # this the forest's scenario part, which generates
# fgun.addObj(bugtouch)
# fgun.addObj(grassmell)  # later, an animal roaming into the forest will be added

ta.bindScenario(fgun)
ta.turnonLearning = False
q = TQueue()  # central queue
jav = JavanaCitta(SenseType.nose, ta.tqueue)  # bind to ta's tqueue
ta.setjavana(jav, ta.onJavana)
regiscitta = RegistrationCitta()  # bind to ta's tqueue
regiscitta.setBeing(ta)
ta.setregistration(regiscitta, ta.onRegistration)

# control the scen with animal entries
animal = SmellOdor(SmellType.good, 10, 'other', tickclock)

startThread = False
if startThread:
    ta.run(startThread)
else:  # sequential run, easy to debug
    ta.realtime = False
    odor_list = list(BeingTick.body_odor.keys())
    endT = num_life*life_nofood
    deadtimes = np.zeros(num_tick)
    deadtime_list = []
    num_dead = 0
    for jtick in range(num_tick):  # each tick is one path
        fgun.roam(endT)
        if len(fgun.atimes) == 0:
            # no animal comes out, count as dead
            deadtimes[jtick] = life_nofood
            num_dead += 1
            deadtime_list.append(life_nofood)
            continue
        idx_arr = 0
        ta.init()
        tickclock.reset()
        j = 0
        while j < endT:
        #for j in range(endT):
            if ta.isdead():
                deadtimes[jtick] = j
                deadtime_list.append(j)
                num_dead += 1
                tickclock.tick()
                break
            # need to find next arrival after current clock time as jump delay costs time
            idx_arr = np.searchsorted(fgun.atimes, j, side='left')
            if idx_arr == len(fgun.atimes) - 1:
                break;
            if j == int(fgun.atimes[idx_arr]): # use == to capture misses
                # Animal arrives,let it run 5-door process
                aid = int(fgun.aids[idx_arr])
                odorstr = odor_list[aid]
                # make intensity random as well
                odor_intensity = 5 # np.random.randint(1, 10)
                # we could introduce this animal into the forest
                animal.set_intensity(odor_intensity)
                animal.set_odor(odorstr)
                # now let the animal enter the forrest
                fgun.addObj(animal)  #indeed add to scenario
                # need to post events out of the run thread for testing purposes
                evt = fgun.post(ta.tqueue)
                # how long the animal stays before it leaves
                # animal_stay = Ran.randint(1, 10)  # stay in ticks
                ta.run(startThread)
                # tickclock.sleep(5)  # number of ticks to sleep on
                fgun.removeObj(animal)   # animal leaves
                if idx_arr<len(fgun.atimes)-1:
                    idx_arr += 1  #wait for next animal
                    # if int(fgun.atimes[idx_arr])<=j and idx_arr<len(fgun.atimes)-1:
                    #     idx_arr += 1  # to overcome duplicate records in atimes
            tickclock.tick()
            j = tickclock.current()

    # get statistics of tick deadtimes
    deadtime_mean = np.mean(deadtimes[deadtimes>0])
    print('\nSummary:')
    print('ta.life_nofood=',life_nofood)
    print('ta.time_nohunger =', time_nohunger)
    print('ta.time_jump =', ta.time_jump)
    print('average_arr_interval =', average_arr_interval)
    print('tick population tested =', num_tick)
    print('number of ticks died =', num_dead)
    print('tick die on average = ', deadtime_mean)
    print('times of ticks died =', deadtime_list)
