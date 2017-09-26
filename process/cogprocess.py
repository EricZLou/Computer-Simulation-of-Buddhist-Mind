# Cognitive process

# from process.globalvar import *
# from process.bhost import *
# from process.bavanga import Bavanga
# from senses.citta import *
# from senses.citta_eye import *
# from senses.being import Being
#
class CognitiveProcess(object):
    def __init__(self, being, ticks=0):
        # robj: rupa object
        self.ticks = ticks
        self.being = being
        self.determine_citta = None
        self.javana_citta = None
        self.regis_citta = None
        self.sobj = None  # leave to door and mind proc to set
        self.debug = False

    def tick(self, n=1):
        self.ticks += n

    def doregistration(self):
        if self.javana_citta is None:
            print('registrating...')
        else:
            self.regis_citta.callback_func(self.sobj)
        # regis means short term or long term memory?
        #self.being.addObj(self.robj.name, self.robj)
        return 'Rg Rg '

    def dojavana(self, ba):
        if self.javana_citta is None:
            print('going javana...')
        else:
            self.javana_citta.callback_func(self.sobj)
        return 'J1 J2 J3 J4 J5 J6 J7 '

    # note, dodetermination is left to derived class to implement
    def dodetermination(self, evt):
        if self.determine_citta is None:
            print('do determination...')
        else:
            self.determine_citta.callback_func(self.sobj)
        return ''

    def dofutile(self, ba):
        ba.vibrate()
        self.tick()
        if self.debug:
            print('vibrating...')
        return 'P V '