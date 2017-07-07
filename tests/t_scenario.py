# test worldly objects in a scenario

from worldly.scenario import Scenario
from worldly.visible_form import VisibleForm
from worldly.env import Env


def get_scen():
    # create objects appearing in a scenario
    tree = VisibleForm(10,'round','green')
    gun = VisibleForm(3, 'handgun-shaped','silver')
    car = VisibleForm(8, '', 'red')
    person = VisibleForm(5, 'fat', 'white')
    dog = VisibleForm(2, 'round', 'beige')

    # create an env
    env = Env(10, 10, 10, 10)

    # create a scenario and print it out
    scen = Scenario(env, 'House')
    scen.addObj(tree)
    scen.addObj(gun)
    scen.addObj(car)
    scen.addObj(person)
    scen.addObj(dog)

    # # we can also bind an obj with a scenario to make them connected
    # tree.bindScenario(scen)
    # gun.bindScenario(scen)
    # car.bindScenario(scen)
    # person.bindScenario(scen)
    # dog.bindScenario(scen)
    #
    return scen

myscen = get_scen()
myscen.print()
