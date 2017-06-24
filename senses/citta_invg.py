# Investigating citta:
#     This is the one that investigate and evaluate an object's features
#       which are then fed to determining citta to determine the object by name
#       i.e., perception

from senses.citta import Citta

class InvestigatingCitta(Citta):
    def __init__(self):
        super(Citta, self).__init__(self)
        self.features = {} # use dictionary to denote a series of features by label and value

    # evaluate and fill up features for the object associated with the citta
    def evaluate(self):
        # default to equinimity
        self.features['sample']=3

    # compare object 1 to see if it has the same features as the citta's object
    def sameFeatures(self, obj1):
        # do work
        return True

    # compare object 1 to see if it is considered similar
    def isSimilar(self, obj1):
        # do work
        return True


# Determining citta:
#     This determines an object by name, i.e., perception


class DetrminingCitta(Citta):
    def __init__(self):
        super(Citta, self).__init__(self)
        self.features = {}  # use dictionary to denote a series of features by label and value

