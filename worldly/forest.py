#
# Purpose: Forest where animals randomly roam
#           keep the scenario. animal gets into the scenario only when it arrives
#
import time
import numpy.random as Ran
import pandas as pd
from senses.events import SenseEvent
from senses.ticked_object import TickedObj
from worldly.scenario import Scenario


class Forest(Scenario):
    # need to maintain a clock
    def __init__(self, tclock, env):
        super().__init__(tclock, env, 'South Africa')
        self.aids = []   # animal id sequence
        self.atimes = []  # animal appearance time sequence
        self.animals = []

    def addAnimal(self, ann):
        self.animals.append(ann)

    # animals are added to Scenarios
    def roam(self, endT):
        # given an endT, simulate all animal appearences prior to that and sort
        cols = ['a_id','a_arrival']
        df = pd.DataFrame(columns=cols)  # empty dataframe
        for j in range(0,len(self.animals)):
            anm = self.animals[j]
            ts =  anm.arrivalsBefore(endT)
            aid = ts*0+j
#            df1 = pd.DataFrame(aid, ts, columns=cols)
            df1 = pd.DataFrame({'a_id':aid, 'a_arrival':ts})
            df = df.append(df1)
        #df.reset_index()
        df2 = df.sort_values(['a_arrival'])
        df3 = pd.DataFrame(df2.groupby(by='a_arrival').a_id.max())
        # need to make sure it's unique a_arrival, then pick up the one with highest value
        self.atimes = list(df2['a_arrival'].unique())
        self.aids = list(df3['a_id'])
