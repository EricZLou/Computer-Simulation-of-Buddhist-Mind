# Sense object, images of rupa objects such as visibleform, sound, etc.

from senses.sense_base import *
from senses.ticked_object import TickedObj


class SenseObj(TickedObj):
    def __init__(self, basetype, obj, env, tickclock, greatness=0):
        super().__init__(tickclock)
        # dt is sampling datetime
        self.basetype = basetype  #enum sensory organ as basetype
        self.obj = obj # obj like visible form etc.
        self.env = env # obj env, light etc.
        self.greatness = greatness

    def queryObjGreatness(self):
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        return self.greatness

    def computeObjGreatness(self):
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = 0

    def makejson(self):
        # note, name using rupa object's name; env taking theme;
        jdic = {'basetype':self.basetype, 'name': self.obj.name, 'env':self.env.theme, 'greatness':self.greatness}
        return jdic

#-------------------------------------
class SenseObjEye(SenseObj):
    # light condition: 0 dark, 1 light dark, 2 light, 3 bright
    def __init__(self, basetype, visibleform, light, tickclock):
        super().__init__(basetype, visibleform, light, tickclock)
        self.light = light

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.light


#-------------------------------------
class SenseObjEar(SenseObj):
    # air or media condition: 0 vaccum, 1 rare/sparse, 2 thin air, 3 dense air
    def __init__(self, basetype, sounds, air, tickclock):
        super().__init__(basetype, sounds, air, tickclock)
        self.air = air

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.air


#-------------------------------------
class SenseObjNose(SenseObj):
    # air or media condition: 0 vaccum, 1 rare/sparse, 2 thin air, 3 dense air
    def __init__(self, basetype, smell, wind, tickclock):
        super().__init__(basetype, smell, wind, tickclock)
        self.wind = wind

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.wind


#-------------------------------------
class SenseObjTongue(SenseObj):
    # air or media condition: 0 vaccum, 1 rare/sparse, 2 thin air, 3 dense air
    def __init__(self, basetype, taste, water, tickclock):
        super().__init__(basetype, taste, water, tickclock)
        self.water = water

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.water


#-------------------------------------
class SenseObjBody(SenseObj):
    # air or media condition: 0 vaccum, 1 rare/sparse, 2 thin air, 3 dense air
    def __init__(self, basetype, touch, earth, tickclock):
        super().__init__(basetype, touch, earth, tickclock)
        self.earth = earth

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.earth
