# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


class RupaObj(object):
    units_const = 17
    unit_time = 1000  # in ms in Python

    def __init__(self, dt, scenario=None):
        # dt is sampling datetime
        self.startdt = dt
        self.scenario = scenario    # scenario where the obj locates
        self.name = 'null'  #obj identified by a name or concept
        self.features_dc = {} # dictionary of things
        self.ticks = 0  # allowing direct count of ticks or time

    def tick(self, n=1):
        self.ticks += n
        if self.ticks > RupaObj.units_const:
            self.ticks = self.ticks % RupaObj.units_const

    def reset(self):
        self.ticks = 0

    def ticksgone(self, dt1=0):
        # if dt1=0 or default, use ticks, otehrwise use time
        if dt1 > 0:
            time_lapse  = dt1-self.startdt
            units = int(time_lapse/RupaObj.unit_time)
            return units
        else:
            return self.ticks

    def ticksleft(self, dt1):
        return RupaObj.units_const - self.ticksgone(dt1)

    def addFeature(self, key, value):
        self.features_dc[key]=value

    def bindScenario(self, scenario):
        self.scenario = scenario    # scenario where the obj locates

    def features(self):
        #features defining the obj
        return self.features_dc

    def print(self):
        print(self.name)
        for kv in self.features_dc.items():
            print(kv[0]+ ":", kv[1])