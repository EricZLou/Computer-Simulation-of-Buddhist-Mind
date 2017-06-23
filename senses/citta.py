# citta base

class Citta(object):
    def __init__(self, obj, base):
        self.cetasikas = [] # list of cetasikas by names
        self.obj = obj
        self.base = base

# --------------------------------------------
#   ReceivingCitta generates feelings: pleasant, equinimity, unpleasant: 1, 0, -1

class ReceivingCitta(Citta):
    def __init__(self):
        super(Citta, self).__init__(self)

    def feel(self):
        # default to equinimity
        return 0