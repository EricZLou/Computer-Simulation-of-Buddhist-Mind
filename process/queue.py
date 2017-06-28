# FIFO timed queue class, utilizing a linked list

import datetime
from process.globalvar import *

class TNode(object):
    def __init__(self, item=None, tick=0):
        self.item = item
        self.tick0 = tick # tracks note creation dt, not necessarily item's dt.
        self.next = None
        self.previous = None

    def remaininglife(self, t1):
        time_lapse  = t1-self.tick0
        return max(0,g_tick_units-time_lapse)


class TQueue(object):
    # timed queue. Want to check how long each event stays on the queue
    min_life_units = 3

    def __init__(self, dt=0):
        self.len = 0
        self.head = None
        self.tail = None
        self.startdt = dt
        self.ticks = 0  # support both ticks and datetime operations

    def tick(self, n=1):
        self.ticks += n

    def post(self, x):
        newNode = TNode(x, self.ticks)
        newNode.next = None
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.len = self.len + 1

    def refresh(self):
        # delete expired items
        while self.len > 0:
            if self.head.remaininglife(self.ticks) < TQueue.min_life_units:
                self.getitem()
            else:
                break

    def get(self):
        # get the first item that has remaining life>0
        self.refresh()
        return self.getitem()

    def getitem(self):
        # usual get, doesn't care about life
        item = self.head.item
        self.head = self.head.next
        self.len = self.len - 1
        if self.len == 0:
            self.last = None
        return item

    def front(self):
        if self.len>0:
            return self.head.item
        else:
            return self.head  # None any way

    def size(self):
        return self.len