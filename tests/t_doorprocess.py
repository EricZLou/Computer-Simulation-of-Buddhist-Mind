# test worldly objects in a scenario

from worldly.visible_form import VisibleForm
from process.door_process import FiveDoorProcess
from process.mind_process import MindProcess
from process.bavanga import Bavanga
from senses.being import Being
from senses.citta import Citta
from senses.sense_base import *
from worldly.env import Env
from process.basics import *

# build 5 sense organs
eye = SenseEye([10, 10])
ear = SenseEar([10, 10])
nose = SenseNose(10)
tongue = SenseTongue(10)
body = SenseBody(10)
# build citta/bavanga, and being
banvaga_citta = Citta()
bavanga = Bavanga(banvaga_citta)
being = Being(eye, ear, nose, tongue, body, bavanga)
# build a test rupa object and its environment
tree = VisibleForm(10, 'round', 'green')
vobj = tree
env = Env(10,10,10,10,'garden')
# build a 5-d process
door5 = FiveDoorProcess(being, SenseType.eye, vobj, env)

test5door = True

if test5door:
    # test five-door process
    for j in range(17):
        door5 = FiveDoorProcess(being, SenseType.eye, vobj, env)
        door5.tick(j)
        ticksgone = door5.sobj.ticksgone()
        print('----ticks gone=',j, ticksgone)
        door5.run()
        #vobj.reset()
else:
    # test mind-door process
    for j in range(17):
        door5 = MindProcess(being, vobj, env)
        vobj.tick(j)
        ticksgone = door5.sobj.ticksgone()
        print('----ticks gone=',j, ticksgone)
        door5.run()
        vobj.reset()

# test fine object--no javanna
# test great object--no registration
# test futile object--everything
