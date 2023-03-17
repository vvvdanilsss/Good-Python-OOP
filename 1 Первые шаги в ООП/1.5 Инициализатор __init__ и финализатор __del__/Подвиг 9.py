"""
Подвиг 9. Вам необходимо реализовать односвязный список (не список языка
Python, объекты в списке не хранить, а формировать связанную структуру,
показанную на рисунке) из объектов класса ListObject:



Для этого объявите в программе класс ListObject, объекты которого создаются
командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего
объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему
объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data)
хранятся строки из списка lst_in (первая строка в первом объекте, вторая -
во втором и  т.д.). На первый добавленный объект класса ListObject должна
ссылаться переменная head_obj.

P.S. В программе что-либо выводить на экран не нужно.
"""
import sys


class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])
obj = head_obj

for _ in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[_])
    obj.link(obj_new)
    obj = obj_new