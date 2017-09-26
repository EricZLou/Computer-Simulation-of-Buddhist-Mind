# Budhist being - here tick:
#   A tick has three senses: nose, tongue and body. No eye and ear.
#   its purpose is simple: to suck blood from animals to feed itself
#


import numpy as np
from senses.being import Being
import process.globalvar as gvar
from process.basics import *
from senses.cetasika import *


class TickExperience(object):
    # simple structure to record tick's odor drive experience
    def __init__(self):
        self.score_v =  []
        self.dt_v = []


class BeingTick(Being):
    Num_Food = 10000  # how many times tick has food until it dies
    nb_odor = 12  # num of body odor
    body_odor = {'ox':1, 'rabbit':7, 'man':10, 'deer':6, 'groundhog':1,
                 'mice':5, 'sheep':8, 'fox':2, 'elephant':1, 'monkey':3, 'dog':9,'other':0}
    body_roamrate = {'ox':2, 'rabbit':6, 'man':1, 'deer':5, 'groundhog':4,
                 'mice':8, 'sheep':3, 'fox':5, 'elephant':4, 'monkey':7, 'dog':1,'other':10}
    q_value = 0.9
    decay_rate = 0*0.66/1000 # here 1000 is unit_time

    def __init__(self, nose, tongue, body, tclock, interval=gvar.g_thread_interval):
        super().__init__(None, None, nose, tongue, body, tclock, interval)
        self.turnonLearning = False
        self.life_nofood = 100  # from last food to die due to hunger
        self.time_nohunger = 50  # from last food to feel hungry
        self.time_jump = 5  # time it takes to jump off, latch on, drill blood, and get back to twig
        self.tgt_favor = 1  # when favor> this, jump off. will be dynamically updated as experiences build
        self.tgt_intensity = 1
        self.tgt_favor_food = 0  # when favor > this, consider a meal
        self.odor_experience = {}  # dic to keep odor experiences
        self.count_vg = 0 #very great object/registration count
        # init with empty TickExpereince
        for odortype in BeingTick.body_odor.keys():
            self.odor_experience[odortype] = TickExperience()
        self.tlastfood = -self.time_nohunger*0   # clock for last food, start w/ hungry mode
        self.numfood = 0

    def init(self):
        self.dead = False  # this is from Being
        self.tgt_favor = 1  # these are targets and will be dynamically updated as experiences build
        self.tgt_intensity = 1
        self.odor_experience = {}  # dic to keep odor experiences
        self.count_vg = 0 #very great object/registration count
        # init with empty TickExpereince
        for odortype in BeingTick.body_odor.keys():
            self.odor_experience[odortype] = TickExperience()
        self.tlastfood = -self.time_nohunger*0   # clock for last food, start w/ hungry mode
        self.numfood = 0

    # callback functions for cittas
    def onJavana(self, sobj):
        if sobj.basetype == DoorType.tongue:
            # if it is a taste obj, see if this is blood or something favors
            # score = self.findExperience(sobj)
            print('\nJavana-tongue:')
        elif sobj.basetype == DoorType.body:
            # if it's a touch obj, see if something we can bite it on
            print('\nJavana-body:')
        elif sobj.basetype==DoorType.nose:
            self.javana_citta.score = -1  # signal for not to memorize it
            if self.ishungry() and (not self.isdead()):
                # if it is a smell obj, see if expereince tells we shall fall for it
                odor_obj = sobj.obj
                smell_type = odor_obj.smell
                odor_type = odor_obj.odor
                odor_name = odor_obj.name
                odor_intensity = odor_obj.intensity
                jstr = odor_obj.makejson()
                # note we already have a favor score in favor_odor
                favor = BeingTick.body_odor[odor_type]
                # if favor greater than 3 and intensity > 5, falls! This needs to be learnt!
                if favor>self.tgt_favor and odor_intensity>self.tgt_intensity:
                    self.javana_citta.addCetasika(CetasikaType.Volition)
                    self.javana_citta.score = favor
                    if favor>self.tgt_favor_food:
                        self.feed()
                    self.tclock.tick(self.time_jump)
                    # could update tgt_favor or intensity here
                #print('\nJavana-nose:'+str(jstr))
        else:
            print('Tick: sense not supported!')

    # callback functions for registration citta
    def onRegistration(self, sobj):
        if self.javana_citta.score > 0:  # used as a flag
            self.count_vg += 1   #coutn very great objects
            if self.numfood==BeingTick.Num_Food:
                self.dead = True
                print('Tick finishes food three times--done :-( !')
                return

            if not self.turnonLearning:
                return

            # add to experiences
            if self.javana_citta.score > 0 and sobj.basetype == DoorType.nose:
                odor_obj = sobj.obj
                smell_type = odor_obj.smell
                odor_type = odor_obj.odor
                odor_name = odor_obj.name
                odor_intensity = odor_obj.intensity
                self.odor_experience[odor_type].score_v.append(self.javana_citta.score)
                self.odor_experience[odor_type].dt_v.append(sobj.obj.tickclock.current())
                # self.memorize(sobj)  # for our limited purposes, experience is all that matter
                self.updateExperience()

    # could update tgt_favor or intensity here
    def updateExperience(self):
        # given the current odor, run its statistics/occurrences
        for odortype in BeingTick.body_odor.keys():
            dt_vec = self.odor_experience[odortype].dt_v
            score_vec = self.odor_experience[odortype].score_v
            if len(score_vec)>10:  #don't update w/o enough sample size
                q_score = self.computeDecayQuantile(dt_vec, score_vec)
                if q_score>self.tgt_favor*1.1:
                    self.tgt_favor = q_score
                    print('Updating odor statistics:', q_score)

    # get a histgram and tile
    def computeDecayQuantile(self, dvec, scorevec):
        deldt = dvec[-1] - np.array(dvec)
        scores = np.exp(-self.decay_rate*deldt)*scorevec
        return np.percentile(scores, self.q_value)

    def ishungry(self):
        return self.tclock.current()-self.tlastfood >= self.time_nohunger

    def isdead(self):
        if not self.dead:
            self.dead = self.tclock.current() - self.tlastfood >= self.life_nofood
            if self.dead:
                print('starved to nill :-(( ')
        return self.dead

    def feed(self):
        self.numfood += 1
        self.tlastfood = self.tclock.current()
        #let's pronounce the animal dead, to be removed from scenario