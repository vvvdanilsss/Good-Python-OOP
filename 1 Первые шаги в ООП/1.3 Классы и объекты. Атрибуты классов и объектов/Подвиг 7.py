"""
Объявите класс с именем Dictionary и определите в нем
следующие атрибуты:

rus: "Питон"
eng: "Python"

Затем, с помощью функции getattr() прочитайте и выведите
на экран значение атрибута rus_word. Если такого атрибута
в классе нет, то функция getattr() должна возвращать
булево значение False.
"""


class Dictionary:
    rus = 'Питон'
    eng = 'Python'


print(getattr(Dictionary, 'rus_word', False))
