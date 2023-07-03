class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Telecast:
    uid = Descriptor()
    name = Descriptor()
    duration = Descriptor()

    def __init__(self, uid: int, name: str, duration: int):
        self.uid = uid
        self.name = name
        self.duration = duration


class TVProgram:
    def __init__(self, chanel_name: str):
        self.chanel_name = chanel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for item in self.items:
            if item.uid == indx:
                self.items.remove(item)


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
