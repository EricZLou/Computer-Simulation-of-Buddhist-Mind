# ObjectInMind: an object capturing what's arising in mind
#     it could be a sense object, like an image of a visible form (kisina);
#     or it could be an ideation/concept; or a sequence of processes with a task, e.g., speaking
#     This is different from citta in that a citta lasts only one moment.
#     An apple object in the physical world has visible form, smell, taste, tough, and sound (biting)
#     a sense object takes on one form of each but the mind has the ability of synthesizing these five
#     sense objects into a concept named 'apple'. It may relate to past experiences, pick apples,
#     buy apples, eat apples, throw apples, make apple pies, etc.
#     how do we model up an apple or apple as a concept, as an object, as an experience?
#     Because such an object is storeable and recallable, it could use the same structure as
#     a memory object, perhaps adding more behaviors on top, so we make it inherit from it or has it.

from senses.sense_base import *
from senses.sense_object import SenseObj
from process.memory import ObjectMemory


class ObjInMind(object):
    def __init__(self, name, duration, env):
        # dt is sampling datetime
        self.name = name  #object name or concept
        self.duration = duration # duration of time in mind
        self.env = env # obj env, light etc.
        # Experience is a set of verbs and their values, captured as dictionary with verbs as keys
        self.exp_dict = {}
        self.objmemory = None  # to be set to ObjectMemory

    def addVerb(self, verb, value):
        self. exp_dict[verb] = value

