# Five door adverting citta
#    fetch an 5-door event when this citta arises

from process.basics import *
from senses.citta import Citta


class CittaDoorAdverting(Citta):
    def __init__(self):
        super().__init__()
        #self.event = pullevent

    def fetch(self, q):
        obj = q.get()
        self.base = obj.base
        self.obj = obj
        return obj

    def arise(self):
        return self.fetch
