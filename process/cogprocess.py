# Cognitive process
# Returns string of steps for each individual part of cog process

# from process.globalvar import *
# from process.bhost import *
# from process.bavanga import Bavanga
# from senses.citta import *
# from senses.citta_eye import *
# from senses.being import Being

class CognitiveProcess(object):
    def __init__(self, being, ticks=0):
        # robj: rupa object
        self.ticks = ticks
        self.being = being

    def tick(self, n=1):
        self.ticks += n

    def doregistration(self):
        print('registrating...')
        # regis means short term or long term memory?
        #self.being.addObj(self.robj.name, self.robj)
        return 'Rg Rg '

    def dojavana(self, ba):
        print('going javana...')
        return 'J1 J2 J3 J4 J5 J6 J7 '

    # note, dodetermination is left to derived class to implement
    def dodetermination(self, ba):
        return ''

    def dofutile(self, ba):
        ba.vibrate();
        self.tick()
        print('vibrating...')
        return 'P V '
