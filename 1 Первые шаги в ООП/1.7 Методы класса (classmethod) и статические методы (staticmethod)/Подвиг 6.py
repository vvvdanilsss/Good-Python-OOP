"""
В программе предполагается реализовать парсер (обработчик) строки с данными
string в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
И предполагается его использовать следующим образом:

res = Loader.parse_format("4, 5, -6", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел.
Например, для заданной строки, должно получиться:

[4, 5, -6]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с
двумя статическими методами:

build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число (метод
возвращает полученное целочисленное значение).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""


class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("4, 5, -6", Factory)
