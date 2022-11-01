"""
Объявите класс с именем Figure и двумя атрибутами:

type_fig: 'ellipse'
color: 'red'

Создайте экземпляр с именем fig1 этого класса и добавьте в него
следующие локальные атрибуты:

start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'

Удалите из экземпляра класса свойство color и выведите на экран
список всех локальных свойств (без значений) объекта fig1 в одну
строчку через пробел в порядке, указанном в задании.
"""


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
setattr(fig1, 'start_pt', (10, 5))
setattr(fig1, 'end_pt', (100, 20))
setattr(fig1, 'color', 'blue')
delattr(fig1, 'color') if 'color' in fig1.__dict__ else None
[print(_, end=' ') for _ in fig1.__dict__]
