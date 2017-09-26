# test worldly objects

import json
from worldly.visible_form import *

tree = VisibleForm(10,VisibleShape.high, VisibleColor.blue)
gun = VisibleForm(3, 'handgun-shaped','silver')
car = VisibleForm(8, '', 'red')
person = VisibleForm(5, 'fat', 'white')
dog = VisibleForm(2, 'round', 'beige')

tree.print()
gun.print()
car.print()
person.print()
dog.print()


# test JSON string deserialize to object
jmsg = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'

class Payload1(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

p = Payload1(jmsg)
print(p)
# the above is in fact a data structure. Class behavior needs to be implemented separately
# so this fits as a Pimpl pattern

# alternatively, with explicit class definition
class Payload(object):
    def __init__(self, action, method, data):
        self.action = action
        self.method = method
        self.data = data

def as_payload(dct):
    return Payload(dct['action'], dct['method'], dct['data'])

payload = json.loads(jmsg, object_hook = as_payload)
print(payload)