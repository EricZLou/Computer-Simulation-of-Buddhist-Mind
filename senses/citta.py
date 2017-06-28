# citta base
from process.basics import *


class Citta(object):

    def __init__(self, obj=None, base=None):
        self.cetasikas = [] # list of cetasikas by names
        self.obj = obj   # sense obj or mind obj, not visible form etc.
        self.base = base  # base obj
        self.wsness = Wholesomeness.variable  # enum


class CittaDoorAdverting(Citta):
    # five door adverting
    def __init__(self):
        super().__init__()

    def fetch(self, q):
        obj = q.get()
        self.base = obj.base
        self.obj = obj
        return

# --------------------------------------------
#   ReceivingCitta generates feelings: pleasant, equinimity, unpleasant: 1, 0, -1

class ReceivingCitta(Citta):
    def __init__(self):
        super(Citta, self).__init__(self)

    def feel(self):
        # default to equinimity
        return Feelings.equnimity