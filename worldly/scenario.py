#
# Purpose: Scenario class creates a scenario where senses come into play
#


class Scenario(object):
    def __init__(self, theme='none'):
        self.theme = theme
        self.objs = []  # obj list

    def addObj(self, obj):
        # obj.bindScenario(self)
        self.objs.append(obj)

    def post(self):
        # this posts sense events from this scenario to central queue
        return 0

    def print(self):
        print(self.theme)
        for obj in self.objs:
            obj.print()
