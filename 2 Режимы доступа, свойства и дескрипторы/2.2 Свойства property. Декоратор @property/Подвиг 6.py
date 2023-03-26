"""
Реализуйте односвязный список (не список Python, не использовать список Python
для хранения объектов), когда один объект ссылается на следующий и так по
цепочке до последнего:

Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj
должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта
принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства
__next;
data - для записи и считывания информации из локального приватного свойства
__data.

При записи необходимо реализовать проверку, что __next будет ссылаться на
объект класса StackObj или значение None. Если проверка не проходит, то
__next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список
пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка (список
из строк локального атрибута __data каждого объекта в порядке их добавления,
или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать
не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']

P.S. В программе требуется объявить только классы. На экран ничего выводить не
нужно.
"""


class StackObj:
    def __init__(self, dt):
        self.__data = None
        self.data = dt
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nt):
        if isinstance(nt, StackObj) or nt is None:
            self.__next = nt

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, pr):
        if isinstance(pr, StackObj) or pr is None:
            self.__prev = pr

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, dt):
        self.__data: str = dt


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.last = obj
        else:
            self.last.next = obj
            obj.prev = self.last
            self.last = obj

    def pop(self):
        if self.top is None:
            return None

        if self.last.prev is None:
            res = self.last
            self.top = None
            self.last = None
            return res

        res = self.last
        self.last = self.last.prev
        self.last.next = None
        return res

    def get_data(self):
        if self.top is None:
            return []

        obj = self.top
        res = [obj.data]
        while obj.next:
            res.append(obj.next.data)
            obj = obj.next

        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
r = st.get_data()
print(r)
