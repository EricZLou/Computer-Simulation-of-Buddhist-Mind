# Five door process
#

from senses.citta_eye import *
from senses.citta_ear import CittaEar
from senses.citta_nose import CittaNose
from senses.citta_tongue import CittaTongue
from senses.citta_body import CittaBody
from process.cogprocess import CognitiveProcess
from senses.citta_rec import CittaReceiving
from senses.citta_invg import DeterminingCitta, InvestigatingCitta
from senses.citta5door import *


class FiveDoorProcess(CognitiveProcess):
    def __init__(self, being, basetype, robj, env, ticks):
        super().__init__(being, ticks)
        self.sobj =  SenseObj(basetype, robj, env, being.tclock)

    def tick(self, n=1):
        # process and sense obj both tick in sync
        self.ticks += n
#        self.sobj.tick(n)

    def run(self):
        ba = self.being.bavanga
        ba.past()
        #self.tick()  # start from past bavanga. count at 1: should leave it to ba.past
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
        if self.debug:
            print('very great object cognitive process')
        str17 = self.dofutile(ba)
        str17 += self.dodetermination(ba)
        str17 += self.dojavana(ba)
        str17 += self.doregistration()
        if self.debug:
            print(str17)

    def javanacourse(self, ba, tickspast):
        # course ending with javana
        print('great object cognitive process-no registration')
        str17='P '
        if tickspast == g_tickpassed_great:
            str17='P P '
        str17 += self.dofutile(ba)
        str17 += self.dodetermination(ba)
        str17 += self.dojavana(ba)
        # might have additional bavanga
        if tickspast < g_tickpassed_great:
            str17 += 'B '
        print(str17)

    def determcourse(self, ba, tickspast):
        # course ending with determination
        print('fine cognitive process-no javana')
        str17='P P P ' # already has three
        for j in range(g_tickpassed_great+1, tickspast):
            str17 += 'P '
        str17 += self.dofutile(ba)
        str17 += self.dodetermination(ba)
        str17 += 'D '
        if tickspast < g_tickpassed_fine:
            str17 += 'D '
            for j in range(tickspast+1, g_tickpassed_fine):
                str17 += 'B '
        else:
            for j in range(tickspast+1, g_tickpassed_fine-1):
                str17 += 'B '
        print(str17)

    def futilecourse(self, ba, tickspast):
        print('very fine cognitive process-no determination')
        str17='P P P P P P P P ' # already has three
        for j in range(g_tickpassed_fine, tickspast):
            str17 += 'P '
        str17 += self.dofutile(ba)
        str17 += 'V '
        for j in range(tickspast, g_tickpassed_veryfine):
            str17 += 'B '
        print(str17)

    def dodetermination(self, ba):
        #5door adverting to pick from central queue. This should be the point where
        #obj is bound. Inpact is just to make aware of the presence of an obj
        base = self.sobj.obj.basetype
        doorAdv = CittaDoorAdverting()
        if base == DoorType.mind:
            print('Wrong door!')
            return
        temp = doorAdv.arise()
        robj = self.sobj.obj
        # now sense citta
        if base == DoorType.eye:
            citta = CittaEye(self.being.eye, robj, self.sobj.env.light)
        elif base == DoorType.ear:
            citta = CittaEar(self.being.eye, robj, self.sobj.env.light)
        elif base == DoorType.nose:
            citta = CittaNose(self.being.eye, robj, self.sobj.env.light)
        elif base == DoorType.tongue:
            citta = CittaTongue(self.being.eye, robj, self.sobj.env.light)
        elif base == DoorType.body:
            citta = CittaBody(self.being.eye, robj, self.sobj.env.light)

        citta.doSense()
        # next arise receiving citta
        recitta =  CittaReceiving()  # each citta when arise costs one tick!
        recitta.go()
        invgcitta = InvestigatingCitta()
        invgcitta.setBeing(self.being)
        invgcitta.go()
        decitta = DeterminingCitta()
        decitta.setBeing(self.being)
        decitta.go()
        if self.debug:
            print('determining...')
        return 'A F E Rc I D '
