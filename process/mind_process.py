# Mind door process - Clear/Non-clear
#   four folds: very clear, clear, obscure, very obscure

from process.globalvar import *
from process.cogprocess import CognitiveProcess
# from process.bhost import *
# from process.bavanga import Bavanga
# from senses.citta import *
# from senses.citta_eye import *
# from senses.being import Being


class MindProcess(CognitiveProcess):
    def __init__(self, being, sobj, ticks=0):
        super().__init__(being, ticks)
        self.sobj = sobj

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
        print('very clear object mind door process')
        str17 = self.dofutile(ba)
        str17 += self.dodetermination(ba)
        str17 += self.dojavana(ba)
        str17 += self.doregistration()
        print(str17)

    def javanacourse(self, ba, tickspast):
        # course ending with javana
        print('clear object mind door process-no registration')
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
        str17 += 'M '
        if tickspast < g_tickpassed_fine:
            str17 += 'M '
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
        ba.arrest();
        self.tick()
        # mind door adverting is the determinaing citta
        print('determining...')
        return 'A M '

# -----------------------------------------------------------------
class ConsequentProcess(MindProcess):
    def __init__(self, being, robj, env, doorproc):
        super().__init__(being, robj, env)
        self.doorproc = doorproc #previous 5door process

    # for consequent sense sphere mind process
    def makeWhole(self):
        return ''

    def makeColor(self):
        return ''

    def makeEntity(self):
        # shape etc.
        return ''

    def makeName(self):
        # grasp name
        return ''
