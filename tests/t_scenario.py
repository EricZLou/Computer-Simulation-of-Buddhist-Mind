# test worldly objects in a scenario

from worldly.scenario import Scenario
from worldly.visible_form import VisibleForm


def get_scen():
    # create objects appearing in a scenario
    tree = VisibleForm(10,'round','green')
    gun = VisibleForm(3, 'handgun-shaped','silver')
    car = VisibleForm(8, '', 'red')
    person = VisibleForm(5, 'fat', 'white')
    dog = VisibleForm(2, 'round', 'beige')

    # create a scenario and print it out
    scen = Scenario('House')
    scen.addObj(tree)
    scen.addObj(gun)
    scen.addObj(car)
    scen.addObj(person)
    scen.addObj(dog)

    # we can also bind an obj with a scenario to make them connected
    tree.bindScenario(scen)
    gun.bindScenario(scen)
    car.bindScenario(scen)
    person.bindScenario(scen)
    dog.bindScenario(scen)

    return scen

myscen = get_scen()
myscen.print()
