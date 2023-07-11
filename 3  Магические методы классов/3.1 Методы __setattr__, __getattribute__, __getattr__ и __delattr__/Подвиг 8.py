class ValidateValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif self.name == '__radius':
            setattr(instance, self.name, value) if value > 0 else None
        else:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Circle:
    x = ValidateValue()
    y = ValidateValue()
    radius = ValidateValue()

    def __init__(self, x: int or float, y: int or float, radius: int or float):
        self.x, self.y = x, y
        self.radius = radius

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10  # Прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
print(circle.radius)
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
print(circle.name)


