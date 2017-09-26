# Javana citta
#    How things work out

from process.basics import *
from senses.citta import Citta
from senses.sense_base import *

class JavanaCitta(Citta):
    # requires a decayed queue
    def __init__(self, basetype, dq):
        super().__init__()
        self.base = makeSenseBase(basetype, [10, 10])  # strength 10
        self.dq = dq
        self.score = 0  #outcome of javana

    def fetch(self, q):
        evt = q.get()
        self.base = makeSenseBase(evt.basetype, [10, 10])
        self.obj = evt.obj
        return evt

    def arise(self):
        if self.debug:
            print('\nJavana arising ...')
        return self.fetch(self.dq)
