"""
Объявите класс с именем Goods и пропишите в нем следующие
атрибуты (переменные):

title: "Мороженое"
weight: 154
tp: "Еда"
price: 1024

Затем, после объявления класса, измените его атрибут price
на значение 2048 и добавьте еще один атрибут:

inflation: 100
"""


class Goods:
    title = 'Мороженое'
    weight = 154
    tp = 'Еда'
    price = 1024


setattr(Goods, 'price', 2048)
setattr(Goods, 'inflation', 100)
