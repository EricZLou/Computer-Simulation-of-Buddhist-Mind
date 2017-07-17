# bavanga stream
# gives values to basic conditions
from enum import Enum


class Wholesomeness(Enum):
    wholesome = 1
    unwholesome = -1
    variable = 0


class ObjectDesirable(Enum):
    undesirable = -1
    desirable = 0
    verydesirable = 1


class Greatness(Enum):
    # physical object
    veryfine = 1
    fine = 2
    great = 3
    verygreat = 4


class Clearness(Enum):
    # mind object
    veryobscure = 1
    obscure = 2
    clear = 3
    veryclear = 4


class Feelings(Enum):
    pleasant = 1
    pain = 2
    equnimity = 3
    joy = 4
    unpleasant = 5


class SenseType(Enum):
    eye = 1
    ear = 2
    nose = 3
    tongue = 4
    body = 5
    mind = 0


class DoorType(Enum):
    eye = 1
    ear = 2
    nose = 3
    tongue = 4
    body = 5
    mind = 0