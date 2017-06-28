# bavanga stream


class Bavanga(object):
    def __init__(self, citta):
        self.citta = citta
        self.ticks = 0

    def bind(self, citta):
        self.citta = citta

    def past(self):
        print('past bavanga-')
        self.ticks += 1

    def vibrate(self):
        print('bavanga vibrates-')
        self.ticks += 1

    def arrest(self):
        print('bavanga arrest-')
        self.ticks += 1

    def sleep(self, nticks):
        print('bavanga sleeps now-')
        self.ticks += nticks
