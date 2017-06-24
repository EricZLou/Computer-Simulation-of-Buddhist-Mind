# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


class RupaObj(object):
    def __init__(self, dt):
        # dt is sampling datetime
        self.startdt = dt
        self.units_const = 17
        self.unit_time = 1000 # in ms in Python
        self.name = ''  #obj identified by a name or concept
        self.features_dc = {} # dictionary of things

    def unitsleft(self, dt1):
        time_lapse  = dt1-self.startdt
        units = int(time_lapse/self.unit_time)
        return max(0,self.units_const-units)

    def addFeature(self, key, value):
        self.features_dc[key]=value

    def features(self):
        #features defining the obj
        return self.features_dc

    def print(self):
        for kv in self.features_dc.items():
            print(kv[0]+ ":", kv[1])