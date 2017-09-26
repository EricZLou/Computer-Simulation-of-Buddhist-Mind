# Investigating citta:
#     This is the one that investigate and evaluate an object's features
#       which are then fed to determining citta to determine the object by name
#       i.e., perception

from senses.citta import Citta


class InvestigatingCitta(Citta):
    # three cittas: wholesome or unwholesome resultant accompanied w equnimity,
    #     plus wholesome resultant with joy
    def __init__(self, iswholesomerslt=True, equnimity=True):
        super().__init__()
        self.features = {} # use dictionary to denote a series of features by label and value
        self.iswholesomerslt = iswholesomerslt
        self.equnimity = equnimity

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
#     To be exact, this is MindDoorAdvertingCitta functions as determining


class DeterminingCitta(Citta):
    def __init__(self):
        super().__init__()
        self.features = {}  # use dictionary to denote a series of features by label and value

    def go(self):
        if self.being is not None:
            return self.being.recall(self.obj)  # Citta.obj, return name
        else:
            print('No being assigned in Determining citta. go() ignored.')

# Registration citta:
#     To be exact, this is citta that performs registration function
#     it could be investigating citta or sense-sphere resultant cittas


class RegistrationCitta(Citta):
    def __init__(self):
        super().__init__()
        self.features = {}  # use dictionary to denote a series of features by label and value

    def go(self):
        if self.being is not None:
            return self.being.memorize(self.obj)  # Citta.obj, return name
        else:
            print('No being assigned in registration citta. go() ignored.')
