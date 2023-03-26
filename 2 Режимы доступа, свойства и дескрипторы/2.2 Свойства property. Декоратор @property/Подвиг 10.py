"""
Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты
этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого
класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class PhoneNumber:
    def __init__(self, number, fio):
        self.number: int = number
        self.fio: str = fio


class PhoneBook:
    def __init__(self):
        self.__phone_list = []

    def add_phone(self, phone):
        self.__phone_list.append(phone)

    def remove_phone(self, indx):
        self.__phone_list.pop(indx)

    def get_phone_list(self):
        return self.__phone_list
