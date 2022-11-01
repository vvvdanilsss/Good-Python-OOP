"""
Объявите пустой класс с именем Car. С помощью функции setattr() добавьте
в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"

Выведите на экран значение атрибута color, используя словарь __dict__
класса Car.
"""


class Car:
    pass


cars = {'model': 'Тойота', 'color': 'Розовый', 'number': 'П111УУ77'}
[setattr(Car, _, cars[_]) for _ in cars]
print(Car.__dict__['color'])
