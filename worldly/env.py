#
# Purpose: Env class creates an env where sense organs operate
#
from process.basics import *

class Env(object):
    def __init__(self, light, air, water, wind, theme=''):
        self.light = light  # for eye
        self.air = air      # for ear
        self.water = water      # for tongue
        self.wind = wind      # for nose
        self.theme = theme

    def lightStrength(self):
        # assume light is already in 1-4 scale
        return Greatness(self.light)

    def airStrength(self):
        # assume air is already in 1-4 scale
        return Greatness(self.air)

    def waterStrength(self):
        # assume light is already in 1-4 scale
        return Greatness(self.water)

    def windStrength(self):
        # assume light is already in 1-4 scale
        return Greatness(self.wind)