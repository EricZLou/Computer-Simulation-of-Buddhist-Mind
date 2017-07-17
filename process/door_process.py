# Five door process
# Uses cogprocess.py
# For the 5 door process, prints full string of steps

from process.globalvar import *
from senses.citta_eye import *
from process.cogprocess import CognitiveProcess
# from process.bhost import *
# from process.bavanga import Bavanga
# from senses.citta import *

class FiveDoorProcess(CognitiveProcess):
    def __init__(self, being, basetype, robj, env, ticks=0):
        super().__init__(being, ticks)
        self.sobj =  SenseObj(being.base(basetype), robj, env)
        self.sobj.tick(ticks)

    def tick(self, n=1):
        # process and sense obj both tick in sync
        self.ticks += n
        self.sobj.tick(n)

    def run(self):
        ba = self.being.bavanga
        ba.past()
        self.tick()  # start from past bavanga. count at 1
        tickspast = self.sobj.ticksgone()
        if tickspast <= g_tickpassed_verygreat:
            self.regcourse(ba)
        elif tickspast <= g_tickpassed_great:
            self.javanacourse(ba, tickspast)
        elif tickspast <= g_tickpassed_fine:
            self.determcourse(ba, tickspast)
        elif tickspast <= g_tickpassed_veryfine:
            self.futilecourse(ba, tickspast)
        else:
            print('nothing')

    def regcourse(self, ba):
        # course ending with registration
        print('very great object cognitive process')
        str17 = self.dofutile(ba)
        str17 = str17 + self.dodetermination(ba)
        str17 = str17 + self.dojavana(ba)
        str17 = str17 + self.doregistration()
        print(str17)

    def javanacourse(self, ba, tickspast):
        # course ending with javana
        print('great object cognitive process-no registration')
        str17='P '
        if tickspast == g_tickpassed_great:
            str17='P P '
        str17 = str17 + self.dofutile(ba)
        str17 = str17 + self.dodetermination(ba)
        str17 = str17 + self.dojavana(ba)
        # might have additional bavanga
        if tickspast < g_tickpassed_great:
            str17 = str17 + 'B '
        print(str17)

    def determcourse(self, ba, tickspast):
        # course ending with determination
        print('fine cognitive process-no javana')
        str17='P P P ' # already has three
        for j in range(g_tickpassed_great+1, tickspast):
            str17 = str17 + 'P '
        str17 = str17 + self.dofutile(ba)
        str17 = str17 + self.dodetermination(ba)
        str17 = str17 +'D '
        if tickspast < g_tickpassed_fine:
            str17 = str17 +'D '
            for j in range(tickspast+1, g_tickpassed_fine):
                str17 = str17 + 'B '
        else:
            for j in range(tickspast+1, g_tickpassed_fine-1):
                str17 = str17 + 'B '
        print(str17)

    def futilecourse(self, ba, tickspast):
        print('very fine cognitive process-no determination')
        str17='P P P P P P P P ' # already has three
        for j in range(g_tickpassed_fine, tickspast):
            str17 = str17 + 'P '
        str17 = str17 + self.dofutile(ba)
        str17 = str17 +'V '
        for j in range(tickspast, g_tickpassed_veryfine):
            str17 = str17 + 'B '
        print(str17)

    def dodetermination(self, ba):
        ba.arrest();
        self.tick()
        #5door adverting to pick from central queue. This should be the point where
        #obj is bound. Inpact is just to make aware of the presence of an obj
        #doorAdv = CittaDoorAdverting()
        # now sense citta
        #citta = CittaEye(self.being.eye, self.robj, self.env.light)
        # next arise receiving citta
        print('determining...')
        return 'A F E Rc I D '
