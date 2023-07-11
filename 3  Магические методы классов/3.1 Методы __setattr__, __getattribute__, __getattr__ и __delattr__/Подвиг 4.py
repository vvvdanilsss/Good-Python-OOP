from typing import Union


class Product:
    id: int = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        obj = super().__new__(cls)
        setattr(obj, 'id', cls.id)
        return obj

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if (key == 'name' and isinstance(value, str)) or key == 'id':
            object.__setattr__(self, key, value)
        elif key in ('weight', 'price') and (isinstance(value, (int, float)) and value > 0):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
