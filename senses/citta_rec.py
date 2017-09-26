# receiving citta:
#

from process.basics import *
from senses.citta import Citta

# --------------------------------------------
#   CittaReceiving generates feelings: pleasant, equinimity, unpleasant: 1, 0, -1

class CittaReceiving(Citta):
    def __init__(self):
        super().__init__()

    def feel(self):
        # default to equinimity
        return Feelings.equnimity