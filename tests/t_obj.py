# test worldly objects

from worldly.visible_form import VisibleForm

tree = VisibleForm(10,'round','green')
gun = VisibleForm(3, 'handgun-shaped','silver')
car = VisibleForm(8, '', 'red')
person = VisibleForm(5, 'fat', 'white')
dog = VisibleForm(2, 'round', 'beige')

tree.print()
gun.print()
car.print()
person.print()
dog.print()