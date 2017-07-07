# test memory setup - worldly objects in a scenario

import json
import utils.jsonencoder as jut
from worldly.scenario import Scenario
from worldly.visible_form import VisibleForm
from worldly.sound_form import SoundForm
from process.memory import *
from tests.t_scenario import get_scen
from senses.being import Being
from senses.sense_base import *

# create a dummy person/being
eye = SenseEye([10, 10])
ear = SenseEar([10, 10])
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
citta0 = None # initial citta
dummy = Being(eye, ear, nose, tongue, body, citta0)

# test json
print('\ntest json dumps ...')
eye_json = json.dumps(eye, default=jut.makeJSON)
print(eye_json)

# create objects appearing in a scenario
tree = VisibleForm(10,'round','green')
dummy.memorize(tree)
tree_json = json.dumps(tree, default=jut.makeJSON)
print(tree_json)

gun = VisibleForm(3, 'handgun-shaped','silver')
dummy.memorize(gun)

car = VisibleForm(8, '', 'red')
dummy.memorize(car)

person = VisibleForm(5, 'fat', 'white')
dummy.memorize(person)

dog = VisibleForm(2, 'round', 'beige')
dummy.memorize(dog)

pitchvoice = SoundForm(10, 'high', 100)
dummy.memorize(pitchvoice)

# test obj recall
print('\ntest recall obj by features-best match ...')
features = tree.features()
print(features)
obj = dummy.recall(features)
obj.print()

print('\ntest recall obj by features- minmatch...')
obj = dummy.recall(pitchvoice.features(),False)
obj.print()