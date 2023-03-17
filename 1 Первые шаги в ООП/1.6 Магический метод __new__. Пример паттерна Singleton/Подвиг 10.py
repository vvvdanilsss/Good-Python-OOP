"""
В программе предполагается реализовать парсер (обработчик) строки (string)
в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

И предполагается его использовать следующим образом:

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
На выходе (в переменной res) ожидается получить список из набора вещественных
чисел. Например, для заданной строки, должно получиться:

[4.0, 5.0, -6.5]

Для реализации этой идеи необходимо вначале программы прописать класс Factory
с двумя методами:

build_sequence(self) - для создания начального пустого списка (метод должен
возвращать пустой список);
build_number(self, string) - для преобразования переданной в метод строки
(string) в вещественное значение (метод должен возвращать полученное
вещественное число).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""


class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
