# TickedObj or Objects endures time.
#    could be real time or a faked tick-clock
import time


class TickClock(object):
    def __init__(self, start=0):
        self.start = start
        self.ticks = start  # current ticks

    def tick(self, n=1):
        self.ticks += n
        return self.ticks

    def current(self):
        return self.ticks

    def reset(self):
        self.start = 0
        self.ticks = 0

    def sleep(self, ntick):
        self.ticks += ntick
        return self.ticks


class TickRealClock(TickClock):
    # use time() to get real time but convert to ticks
    def __init__(self, startdt=time.time(), unit_time=1000.0):
        super().__init__(round(startdt/unit_time))
        self.unit_time = unit_time
        self.startdt = startdt
        self.currentdt = startdt

    def current(self):
        self.currentdt = time.time()
        self.ticks = round(self.currentdt/self.unit_time)
        return self.ticks

    def reset(self):
        super().reset()
        self.startdt = time.time()
        self.currentdt = self.startdt
        self.start = round(self.startdt/self.unit_time)
        self.ticks = self.start

    def sleep(self, ntick):
        units = (ntick*self.unit_time)*1E-3  # unit_time in mil sec
        time.sleep(units)        # sleep in seconds
        return self.current()


class TickedObj(object):
    # clock is too important to have a default. Have to initialize!
    def __init__(self, tickclock, units_const=17):
        self.tickclock = tickclock  # allowing direct count of ticks when not None
        self.init_tick = tickclock.current()
        self.units_const = units_const   # class variables

    def unitsleft(self):
        units = self.tickclock.current() - self.init_tick
        units %= self.units_const
        return max(0,self.units_const-units)

    def tick(self, n=1):
        return self.tickclock.tick(n)

    def reset(self):
        self.tickclock.reset()

    def ticksgone(self):
        units = self.tickclock.current() - self.init_tick
        units %= self.units_const
        return units

    def ticksleft(self):
        return self.unitsleft()
