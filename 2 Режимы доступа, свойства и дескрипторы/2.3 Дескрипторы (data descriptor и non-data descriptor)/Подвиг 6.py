class FloatValue:
    @classmethod
    def verify_val(cls, val):
        if type(value) != float:
            raise TypeError('Присваивать можно только вещественный тип данных.')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, val):
        self.verify_val(val)
        setattr(instance, self.name, val)


class Cell:
    value = FloatValue()

    def __init__(self, initial_value=0.0):
        self.value = initial_value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)

value = 1.0
for row in table.cells:
    for cell in row:
        cell.value = value
        value += 1.0
