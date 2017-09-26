# bavanga stream
from enum import IntEnum


class Wholesomeness(IntEnum):
    wholesome = 1
    unwholesome = -1
    variable = 0


class ObjectDesirable(IntEnum):
    undesirable = -1
    desirable = 0
    verydesirable = 1


class Greatness(IntEnum):
    # physical object
    veryfine = 1
    fine = 2
    great = 3
    verygreat = 4


class Clearness(IntEnum):
    # mind object
    veryobscure = 1
    obscure = 2
    clear = 3
    veryclear = 4


class Feelings(IntEnum):
    pleasant = 1
    pain = 2
    equnimity = 3
    joy = 4
    unpleasant = 5


class SenseType(IntEnum):
    eye = 1
    ear = 2
    nose = 3
    tongue = 4
    body = 5
    mind = 0


class DoorType(IntEnum):
    eye = 1
    ear = 2
    nose = 3
    tongue = 4
    body = 5
    mind = 0