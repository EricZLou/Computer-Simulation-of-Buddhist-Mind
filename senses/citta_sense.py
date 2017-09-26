# citta sense: common base class for 5 sense or 5 door consciousness

from enum import Enum
from process.basics import *
from senses.citta import Citta
from senses.sense_object import *


class CittaSense(Citta):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj):
        super().__init__(base, vobj)
        self.sobj = None   #can't produce yet. derived class does it

    def arise(self):
        # evaluate strength
        if self.debug:
            print('\nSense citta arises...')
        self.sobj.computeObjGreatness()
        return

    def doSense(self):
        # each door/sense should override to do its own things
        # print('do sense.')
        return

    def getTrait(self, trait):
        print('Bad trait')