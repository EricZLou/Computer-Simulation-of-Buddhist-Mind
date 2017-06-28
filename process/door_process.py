# Five door process

from process.globalvar import *
from process.bhost import *
from process.bavanga import Bavanga
from senses.citta import *
from senses.citta_eye import *
from senses.being import Being

class FiveDoorProcess(object):
    def __init__(self, being, robj, env):
        # robj: rupa object
        self.ticks = 0
        self.being = being
        self.robj = robj
        self.env = env

    def tick(self):
        self.ticks += 1
        self.robj.tick()

    def run(self):
        ba = self.being.bavanga
        ba.past()
        self.tick()  # start from past bavanga. count at 1
        tickspast = self.robj.ticksgone()
        if tickspast <= g_tickpassed_verygreat:
            self.regcourse(ba)
        elif tickspast <= g_tickpassed_great:
            self.javanacourse(ba)
        elif tickspast <= g_tickpassed_fine:
            self.determcourse(ba)
        elif tickspast <= g_tickpassed_veryfine:
            self.futilecourse(ba)
        else:
            print('nothing')

    def regcourse(self, ba):
        # course ending with registration
        print('very great object cognitive process')
        self.dodetermination(ba)
        self.dojavana(ba)
        self.doregistration()

    def javanacourse(self, ba):
        # course ending with javana
        print('great object cognitive process-no registration')
        self.dodetermination(ba)
        self.dojavana(ba)
        # might have additional bavanga


    def determcourse(self, ba):
        # course ending with determination
        print('fine cognitive process-no javana')
        self.dodetermination(ba)

    def futilecourse(self, ba):
        print('very fine cognitive process-no determination')
        ba.vibrate();
        self.tick()

    def doregistration(self):
        print('registrating...')
        # regis means short term or long term memory?
        self.being.addObj(self.robj.name, self.robj)

    def dojavana(self, ba):
        print('going javana...')

    def dodetermination(self, ba):
        ba.vibrate();
        self.tick()
        ba.arrest();
        self.tick()
        #5door adverting to pick from central queue. This should be the point where
        #obj is bound. Inpact is just to make aware of the presence of an obj
        doorAdv = CittaDoorAdverting()
        # now sense citta
        citta = CittaEye(self.being.eye, self.robj, self.env.light)
        # next arise receiving citta
        print('determining...')
