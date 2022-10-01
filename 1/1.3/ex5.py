class Car:
    pass


cars = {'model': 'Тойота', 'color': 'Розовый', 'number': 'П111УУ77'}
[setattr(Car, _, cars[_]) for _ in cars]
print(Car.__dict__['color'])