"""
В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты
командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name
объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная
TYPE_OS = 1 и объекты класса DialogLinux, если переменная TYPE_OS не равна 1.
При этом, переменная TYPE_OS может меняться в последующих строчках программы.
Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
"""

TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = None
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        obj.name = args[0]
        return obj

