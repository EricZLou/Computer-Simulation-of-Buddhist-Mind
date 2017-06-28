# test timed queue

import process.queue as queue
import time
from tests.t_scenario import get_scen

# create a scenario with objects
scen = get_scen()
nobj = len(scen.objs)
# create a queue, add scenario's objs with interval of time in ticks
tq = queue.TQueue()
for i in range(nobj):
    time.sleep(queue.g_tick_time*2)
    tq.tick(2)
    tq.post(scen.objs[i])

# test obj remaining life and see how it expires
qlen = tq.size()
for i in range(50):
    tq.tick()  # maybe tick should trigger refresh automatically
    tq.refresh()
    if qlen > tq.size():
        print('An item expired: ticks = ', i)
        front = tq.front()
        front.print()
        qlen = tq.size()

