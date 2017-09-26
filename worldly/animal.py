#
# Purpose: animals in a forest, odor, roaming rate and arrival time
#
import numpy as np
import numpy.random as Ran
from worldly.smell_form import SmellOdor


class Animal(object):
    # need to maintain a clock
    def __init__(self, name, odor, roamingrate):
        self.name = name
        self.odor = odor
        self.roamingrate = roamingrate

    def nextarrival(self):
        u = Ran.uniform()
        tao = - np.log(1.0-u)/self.roamingrate
        return tao

    def arrivals(self, n):
        u = Ran.uniform(0.0, 1.0, n)
        tao = - np.log(1.0-u)/self.roamingrate
        return tao

    def arrivalsBefore(self, T):
        n = round(4*T*self.roamingrate)
        #Ran.seed(20000611)   #for debug purposes
        #u = Ran.uniform(0., 1., n)
        #tao = np.round(- np.log(1.0-u)/self.roamingrate)
        tao = np.random.exponential(1/self.roamingrate, n)
        tao1 = np.cumsum(np.round(tao))
        tao_r = tao1[tao1<T]
        return tao_r