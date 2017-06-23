#
# Purpose: Scenario class creates a scenario where senses come into play
#


class Scenario(object):
    def __init__(self):
        self.theme = 0

    def post(self):
        # this posts sense events from this scenario to central queue
        return 0
