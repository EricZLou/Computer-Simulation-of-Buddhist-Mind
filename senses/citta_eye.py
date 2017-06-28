# citta eye
from process.basics import *
from senses.citta import Citta
from senses.sense_object import *


class CittaEye(Citta):
    # base (organ)+vobj+light to make a visible sense_obj
    # key function is to create a sense obj linked to visible form
    def __init__(self, base, vobj, light):
        super().__init__(self, base)
        self.obj = SenseObjEye(base, vobj, light)

    def arise(self):
        # evaluate strength
        self.senseobj.computeObjGreatness()
        return

